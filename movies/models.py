from django.db import models

class Movie(models.Model):
    title = models.CharField(max_length=255)
    genres = models.CharField(max_length=255)
    synopsis = models.TextField(blank=True, null=True)
    poster_path = models.CharField(max_length=255, blank=True, null=True)
    backdrop_path = models.CharField(max_length=255, blank=True, null=True)
    vote_average = models.FloatField(default=0.0)

    def __str__(self):
        return self.title

    @property
    def genres_list(self):
        if self.genres:
            return [g.strip() for g in self.genres.split('|')]
        return []
