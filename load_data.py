import os
import django
import pandas as pd


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'cinerec.settings')
django.setup()

from movies.models import Movie
from ratings.models import Rating
from django.contrib.auth.models import User

def run():
    # 1. Import Movies
    print("Mengimport data film...")
    movies_df = pd.read_csv('data/movies.csv')
    
    for _, row in movies_df.iterrows():
        # Menggunakan get_or_create agar tidak duplikat jika dijalankan ulang
        Movie.objects.get_or_create(
            id=row['movieId'], 
            defaults={
                'title': row['title'],
                'genres': row['genres']
            }
        )

    # 2. Import Ratings 
    print("Mengimport data ratings...")
    ratings_df = pd.read_csv('data/ratings.csv').head(10000)
    
    for _, row in ratings_df.iterrows():
        # Buat user dummy berdasarkan userId di CSV (contoh: user_1, user_2)
        user_obj, _ = User.objects.get_or_create(username=f"user_{int(row['userId'])}")
        
        try:
            movie_obj = Movie.objects.get(id=row['movieId'])
            Rating.objects.get_or_create(
                user=user_obj,
                movie=movie_obj,
                defaults={'rating': row['rating']}
            )
        except Movie.DoesNotExist:
            continue

    print("Selesai! Data berhasil masuk ke database.")

if __name__ == "__main__":
    run()