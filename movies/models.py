from django.db import models

class Movie(models.Model):
    title = models.CharField(max_length=255)
    genre = models.CharField(max_length=255)
    synopsis = models.TextField(blank=True)

    def __str__(self):
        return self.title
