from django.contrib import admin
from django.urls import path, include
from django.conf import settings # <-- Tambahkan ini
from django.conf.urls.static import static # <-- Tambahkan ini

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('', include('recomendations.urls')),
]

# <-- Tambahkan blok ini di paling bawah
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)