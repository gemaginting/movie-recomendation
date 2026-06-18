from django.shortcuts import render, get_object_or_404, redirect
from movies.models import Movie
from ratings.models import Rating
from accounts.models import Profile
from .utils import get_cbf_cold_start, get_svd_recommendations

def homepage(request):
    recommendations = []
    trending_movies = Movie.objects.all().order_by('-vote_average')[:10]
    genres_list = ['Action', 'Adventure', 'Animation', 'Comedy', 'Crime', 'Documentary', 'Drama', 'Family', 'Fantasy', 'History', 'Horror', 'Music', 'Mystery', 'Romance', 'Sci-Fi', 'Thriller', 'War', 'Western']
    
    recom_method = "Umum"
    because_you_liked = None
    cbf_recommendations = []
    
    if request.user.is_authenticated:
        u_id = request.user.id
        user_ratings = Rating.objects.filter(user_id=u_id).order_by('-rating')
        count = user_ratings.count()
        
        # 1. Main Recommendation (SVD or Cold Start)
        if count < 5:
            recom_method = "Content-Based (Cold Start)"
            profile = getattr(request.user, 'profile', None)
            if profile and profile.preferred_genre:
                user_genres = [g.strip() for g in profile.preferred_genre.split('|') if g.strip()]
            else:
                user_genres = ['Action', 'Adventure'] # Fallback
            recommendations = get_cbf_cold_start(user_genres, n=12)
        else:
            recom_method = "SVD Collaborative Filtering"
            recommendations = get_svd_recommendations(u_id, n=12)
            
        # 2. Content-Based Specific (Because You Liked)
        if count > 0:
            top_movie = user_ratings.first().movie
            because_you_liked = top_movie.title
            cbf_recommendations = get_cbf_cold_start(top_movie.genres.split(','), n=6) # Mocking CBF with genre filter
            
    else:
        raw_recoms = Movie.objects.all().order_by('-vote_average')[:30]
        recommendations = []
        for m in raw_recoms:
            recommendations.append({
                'id': m.id,
                'title': m.title,
                'genres': m.genres,
                'poster_path': m.poster_path,
                'backdrop_path': m.backdrop_path,
                'vote_average': m.vote_average,
                'rating_5': round(m.vote_average / 2, 1) if m.vote_average else 0
            })

    return render(request, 'recomendations/index.html', {
        'recommendations': recommendations,
        'trending': trending_movies,
        'genres': genres_list,
        'because_you_liked': because_you_liked,
        'cbf_recommendations': cbf_recommendations,
        'method': recom_method
    })

def movie_details(request, movie_id):
    movie = get_object_or_404(Movie, id=movie_id)
    user_rating = None

    if request.user.is_authenticated:
        # Cek apakah user sudah pernah merating film ini sebelumnya
        existing_rating = Rating.objects.filter(user=request.user, movie=movie).first()
        if existing_rating:
            user_rating = existing_rating.rating

        # Jika user menekan tombol "Simpan Rating"
        if request.method == 'POST':
            score = request.POST.get('rating_score')
            if score:
                # Simpan atau update rating ke database
                Rating.objects.update_or_create(
                    user=request.user,
                    movie=movie,
                    defaults={'rating': float(score)}
                )
                # Refresh halaman setelah menyimpan
                return redirect('movie_details', movie_id=movie.id)

    return render(request, 'recomendations/movie_details.html', {
        'movie': movie,
        'user_rating': user_rating
    })