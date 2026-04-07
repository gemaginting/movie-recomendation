import pandas as pd
import numpy as np
from movies.models import Movie
from ratings.models import Rating
from surprise import SVD, Dataset, Reader
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.preprocessing import MultiLabelBinarizer

def get_cbf_cold_start(genre_list, n=10):
    """Logika CBF dari notebook untuk user baru"""
    # Ambil data dari database
    movies_qs = Movie.objects.all().values('id', 'title', 'genres')
    df_movies = pd.DataFrame(list(movies_qs))
    
    if df_movies.empty:
        return []

    # Filter berdasarkan genre favorit yang dipilih user
    pattern = '|'.join(genre_list)
    filtered_movies = df_movies[df_movies['genres'].str.contains(pattern, case=False, na=False)]
    
    # Ambil n teratas dan ubah ke list of dictionary agar mudah dibaca Django Template
    return filtered_movies.head(n).to_dict('records')

def get_svd_recommendations(user_id, n=10):
    """Logika SVD dari notebook untuk user lama"""
    # 1. Siapkan data untuk Surprise
    ratings_qs = Rating.objects.all().values('user_id', 'movie_id', 'rating')
    df_ratings = pd.DataFrame(list(ratings_qs))
    
    if df_ratings.empty:
        return []

    reader = Reader(rating_scale=(0.5, 5.0))
    data = Dataset.load_from_df(df_ratings[['user_id', 'movie_id', 'rating']], reader)
    trainset = data.build_full_trainset()

    # 2. Training Model SVD
    model = SVD(n_factors=100, random_state=42)
    model.fit(trainset)

    # 3. Cari film yang belum ditonton user ini
    watched_movie_ids = df_ratings[df_ratings['user_id'] == user_id]['movie_id'].tolist()
    all_movie_ids = Movie.objects.values_list('id', flat=True)
    unwatched_movie_ids = [m_id for m_id in all_movie_ids if m_id not in watched_movie_ids]

    # 4. Prediksi rating untuk film yang belum ditonton
    predictions = []
    for m_id in unwatched_movie_ids:
        pred = model.predict(uid=user_id, iid=m_id)
        predictions.append((m_id, pred.est))

    # Sort dan ambil Top-N
    predictions.sort(key=lambda x: x[1], reverse=True)
    top_movie_ids = [p[0] for p in predictions[:n]]
    
    # Ambil detail film dari database
    result_movies = Movie.objects.filter(id__in=top_movie_ids).values('id','title', 'genres')
    return list(result_movies)