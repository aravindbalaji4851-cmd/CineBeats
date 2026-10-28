from django.db import models
from django.contrib.auth.models import User

from film.models import Movie
# Create your models here.

class Review(models.Model):

    movie = models.ForeignKey(Movie,on_delete=models.CASCADE)

    owner = models.ForeignKey(User,on_delete=models.CASCADE)

    message = models.TextField(max_length=300)

    rating = models.DecimalField(max_digits=3, decimal_places=1)

    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)

    class Meta:

        unique_together = ('movie','owner')
    
    def __str__(self):
        return f"{self.movie}:{self.owner}:{self.message}"

    