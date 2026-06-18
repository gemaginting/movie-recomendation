from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from .models import Profile

def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Buat profile kosong untuk user baru
            Profile.objects.get_or_create(user=user)
            login(request, user) # Langsung login setelah daftar
            return redirect('select_genres') # Arahkan ke pemilihan genre
    else:
        form = UserCreationForm()
    return render(request, 'accounts/register.html', {'form': form})

@login_required
def select_genres_view(request):
    profile, created = Profile.objects.get_or_create(user=request.user)
    
    if request.method == 'POST':
        selected_genres = request.POST.getlist('preferred_genres')
        if selected_genres:
            profile.preferred_genre = '|'.join(selected_genres)
            profile.save()
            return redirect('homepage')
            
    # Mengambil list genre yang aktif sekarang
    current_genres = profile.preferred_genre.split('|') if profile.preferred_genre else []
    genres_list = ['Action', 'Adventure', 'Animation', 'Comedy', 'Crime', 'Documentary', 'Drama', 'Family', 'Fantasy', 'History', 'Horror', 'Music', 'Mystery', 'Romance', 'Sci-Fi', 'Thriller', 'War', 'Western']
    
    return render(request, 'accounts/select_genres.html', {
        'genres': genres_list,
        'current_genres': current_genres
    })

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('homepage')
    else:
        form = AuthenticationForm()
    return render(request, 'accounts/login.html', {'form': form})

def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('homepage')