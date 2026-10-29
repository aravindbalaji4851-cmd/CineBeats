
from rest_framework import serializers


from film.models import Movie

from music.models import Song
from music.serializers import SongSerializer

from response.models import Review
from response.serializers import ReviewSerializer

class MovieSerializer(serializers.ModelSerializer):

    song_count = serializers.SerializerMethodField(read_only=True)

    songs = serializers.SerializerMethodField(read_only=True)

    reviews = serializers.SerializerMethodField(read_only=True)
    
    class Meta:

        model = Movie
        
        fields = '__all__'

        read_only_fields = ['id', 'created_by', 'created_at', 'updated_at']

    def get_song_count(self,obj):

        return Song.objects.filter(movie=obj).count()

    def get_songs(self,obj):

        instances = Song.objects.filter(movie=obj)

        serializer = SongSerializer(instances,many=True)

        return serializer.data

    def get_reviews(self,obj):

        reviews = Review.objects.filter(movie=obj)

        serializer = ReviewSerializer(reviews,many=True)

        return serializer.data
