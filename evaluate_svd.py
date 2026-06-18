import os
import django
import sys

# Setup Django environment
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "cinerec.settings")
django.setup()

import pandas as pd
from ratings.models import Rating
from surprise import SVD, Dataset, Reader
from surprise.model_selection import cross_validate

def evaluate_svd():
    print("Mengambil data rating dari database...")
    ratings_qs = Rating.objects.all().values('user_id', 'movie_id', 'rating')
    df_ratings = pd.DataFrame(list(ratings_qs))
    
    if df_ratings.empty:
        print("Dataset kosong. Tidak bisa melakukan evaluasi.")
        return

    print(f"Total data rating: {len(df_ratings)}")
    
    reader = Reader(rating_scale=(0.5, 5.0))
    data = Dataset.load_from_df(df_ratings[['user_id', 'movie_id', 'rating']], reader)
    
    # Inisialisasi model persis seperti di util.py
    model = SVD(n_factors=100, random_state=42)
    
    print("\nMenjalankan 5-Fold Cross Validation (mohon tunggu sebentar)...")
    results = cross_validate(model, data, measures=['RMSE', 'MAE'], cv=5, verbose=True)
    
    print(f"\n--- HASIL EVALUASI KESELURUHAN ---")
    print(f"Rata-rata RMSE : {results['test_rmse'].mean():.4f}")
    print(f"Rata-rata MAE  : {results['test_mae'].mean():.4f}")

if __name__ == "__main__":
    evaluate_svd()
