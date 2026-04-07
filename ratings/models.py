from django.contrib import admin
from django.contrib.auth.models import User
from movies.models import Movie
from django.db import models

class Rating(models.Model):
    user = models.ForeignKey(User, on_delete= models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete= models.CASCADE)
    rating = models.FloatField()
    review = models.TextField(blank = True)
    timestamp = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return f"{self.user.username} - {self.movie.title} - {self.rating}"
    


    