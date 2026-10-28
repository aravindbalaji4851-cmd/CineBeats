
from django.db import models

from django.contrib.auth.models import User

from film.models import Movie

class Song(models.Model):

    title = models.CharField(max_length=200)

    artist = models.CharField(max_length=200)

    album = models.CharField(max_length=200, null=True)

    genre = models.CharField(max_length=100)

    release_date = models.DateField()

    duration = models.PositiveIntegerField()

    track_number = models.PositiveIntegerField(default=0)

    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)

    created_by = models.ForeignKey(User, on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):

        last_song_object = Song.objects.filter(movie=self.movie).last()

        if last_song_object:
            self.track_number = last_song_object.track_number + 1
        else:
            self.track_number = 1

        return super().save(*args, **kwargs)