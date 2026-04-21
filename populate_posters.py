import os
import django
import requests
import time

import re

# Setup Django Environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'cinerec.settings')
django.setup()

from movies.models import Movie

TMDB_API_KEY = "a189539520653413e00b20e04aa45289"
BASE_URL = "https://api.themoviedb.org/3/search/movie"

def clean_title(title):
    # Tangani format "American President, The (1995)" -> "The American President"
    if ',' in title:
        parts = title.split(',')
        if len(parts) > 1:
            main_title = parts[0].strip()
            suffix = parts[1].strip()
            # Jika ada "The", "A", dsb setelah koma, pindahkan ke depan
            if suffix.lower() in ['the', 'a', 'an']:
                title = f"{suffix} {main_title}"
    return title

def populate_movie_posters():
    movies = Movie.objects.filter(poster_path__isnull=True) | Movie.objects.filter(poster_path="")
    total = movies.count()
    print(f"Ditemukan {total} film tanpa poster.")
    
    for i, movie in enumerate(movies, 1):
        original_title = movie.title
        year = None
        
        # 1. Ekstrak Tahun
        match = re.search(r'\((\d{4})\)', original_title)
        if match:
            year = match.group(1)
            raw_title = original_title.replace(match.group(0), '').strip()
        else:
            raw_title = original_title
            
        # 2. Bersihkan Format Judul (Contoh: "President, The" -> "The President")
        search_title = clean_title(raw_title)
            
        print(f"[{i}/{total}] Mencari: {search_title} ({year if year else 'No Year'})", end=" ", flush=True)
        
        try:
            # PERCOBAAN 1: Dengan Tahun (Lebih Akurat)
            params = {'api_key': TMDB_API_KEY, 'query': search_title}
            if year: params['primary_release_year'] = year
                
            response = requests.get(BASE_URL, params=params)
            data = response.json()
            
            # PERCOBAAN 2: Jika Gagal, coba cari Tanpa Tahun (Sebagai Cadangan)
            if not data.get('results') and year:
                params.pop('primary_release_year')
                response = requests.get(BASE_URL, params=params)
                data = response.json()

            if data.get('results'):
                poster_path = data['results'][0].get('poster_path')
                if poster_path:
                    movie.poster_path = poster_path
                    movie.save()
                    print(f"BERHASIL!")
                else:
                    print("Gagal (poster_path kosong)")
            else:
                print("TIDAK DITEMUKAN")
            
            # Tambah jeda agar lebih stabil (0.25 detik)
            time.sleep(0.25) 
            
        except Exception as e:
            print(f"ERROR: {e}")

if __name__ == "__main__":
    populate_movie_posters()
