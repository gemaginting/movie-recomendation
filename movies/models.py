from django.db import models

class Movie(models.Model):
    title = models.CharField(max_length=255)
    genres = models.CharField(max_length=255)
    synopsis = models.TextField(blank=True, null=True)
    poster_path = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.title
