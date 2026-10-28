from django.db import models
from django.contrib.auth.models import User


class Movie(models.Model):

    title = models.CharField(max_length=200)

    description = models.TextField()

    genre = models.CharField(max_length=100)

    release_date = models.DateField()

    duration = models.PositiveIntegerField()

    rating = models.FloatField()

    created_by = models.ForeignKey(User, on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

