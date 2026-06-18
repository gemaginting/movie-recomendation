import os
import django
import requests
import re

# Setup Django Environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'cinerec.settings')
django.setup()

from movies.models import Movie

# Konfigurasi TMDB
TMDB_API_KEY = "a189539520653413e00b20e04aa45289"
TOP_RATED_URL = "https://api.themoviedb.org/3/movie/top_rated"

# Mapping Genre TMDB ke format dataset (MovieLens style)
GENRE_MAP = {
    28: 'Action', 12: 'Adventure', 16: 'Animation', 35: 'Comedy', 80: 'Crime',
    99: 'Documentary', 18: 'Drama', 10751: 'Children', 14: 'Fantasy',
    36: 'History', 27: 'Horror', 10402: 'Musical', 9648: 'Mystery',
    10749: 'Romance', 878: 'Sci-Fi', 10770: 'Film-Noir', 53: 'Thriller',
    10752: 'War', 37: 'Western'
}

def fetch_and_save_top_rated():
    params = {
        'api_key': TMDB_API_KEY,
        'language': 'en-US',
        'page': 1
    }
    
    print("Mengambil data film rating tertinggi dari TMDB...")
    try:
        response = requests.get(TOP_RATED_URL, params=params)
        response.raise_for_status()
        data = response.json()
        results = data.get('results', [])[:20] # Ambil 20 saja
        
        count = 0
        for movie_data in results:
            title = movie_data.get('title')
            overview = movie_data.get('overview')
            poster_path = movie_data.get('poster_path')
            release_date = movie_data.get('release_date', '')
            genre_ids = movie_data.get('genre_ids', [])
            
            # 1. Format Judul: "Title (Year)" agar konsisten dengan dataset lama
            year = release_date.split('-')[0] if release_date else ""
            formatted_title = f"{title} ({year})" if year else title
            
            # 2. Format Genre: "Genre1|Genre2"
            mapped_genres = [GENRE_MAP.get(gid) for gid in genre_ids if GENRE_MAP.get(gid)]
            if not mapped_genres:
                mapped_genres = ['(no genres listed)']
            genre_string = "|".join(mapped_genres)
            
            # 3. Simpan ke Database
            # Gunakan update_or_create agar film yang sudah ada tetap terupdate ratingnya
            movie_obj, created = Movie.objects.update_or_create(
                title=formatted_title,
                defaults={
                    'genres': genre_string,
                    'synopsis': overview,
                    'poster_path': poster_path,
                    'backdrop_path': movie_data.get('backdrop_path'),
                    'vote_average': movie_data.get('vote_average', 0.0)
                }
            )
            
            if created:
                print(f"[BARU] {formatted_title}")
                count += 1
            else:
                print(f"[SKIP] {formatted_title} (Sudah ada)")
                
        print(f"\nSelesai! Berhasil menambahkan {count} film baru.")
        
    except Exception as e:
        print(f"Terjadi kesalahan: {e}")

if __name__ == "__main__":
    fetch_and_save_top_rated()
