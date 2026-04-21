from django.shortcuts import render, get_object_or_404, redirect
from movies.models import Movie
from ratings.models import Rating
from .utils import get_cbf_cold_start, get_svd_recommendations

def homepage(request):
    recommendations = []
    recom_method = "Umum"
    
    if request.user.is_authenticated:
        u_id = request.user.id
        count = Rating.objects.filter(user_id=u_id).count()
        
        if count < 5:
            recom_method = "Hybrid: Content-Based (Cold Start)"
            recommendations = get_cbf_cold_start(['Action', 'Adventure'], n=10)
        else:
            recom_method = "Hybrid: SVD Collaborative Filtering"
            recommendations = get_svd_recommendations(u_id, n=10)
    else:
        # Ambil 10 film langsung sebagai objek model termasuk poster
        recommendations = Movie.objects.all()[:10].values('id','title', 'genres', 'poster_path')

    return render(request, 'recomendations/index.html', {
        'recommendations': recommendations,
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