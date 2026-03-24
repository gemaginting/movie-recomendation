from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    preferred_genre = models.CharField(max_length=255, blank=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username 