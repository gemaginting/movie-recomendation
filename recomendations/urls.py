from django.urls import path
from . import views

urlpatterns = [
    # Jika pengunjung di halaman awal (''), jalankan fungsi homepage di views.py
    path('', views.homepage, name='homepage'),
    path('movie/<int:movie_id>/', views.movie_details, name='movie_details'),
]