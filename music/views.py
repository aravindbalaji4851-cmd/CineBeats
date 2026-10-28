from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions,authentication
from rest_framework.generics import RetrieveUpdateDestroyAPIView

from music.serializers import SongSerializer
from music.models import Song

from film.models import Movie

class SongListCreateView(APIView):

    authentication_classes = [authentication.TokenAuthentication]

    permission_classes = [permissions.IsAuthenticated]

    def post(self,request,pk=None):

        movie_id = pk

        movie_obj = Movie.objects.get(id=pk)

        form_data = request.data

        serializer = SongSerializer(data=form_data)

        if serializer.is_valid():

            serializer.save(movie=movie_obj,created_by=request.user)

            return Response(data = serializer.data)

        else: return Response(data=serializer.errors)


class SongRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):

    queryset = Song.objects.all()

    serializer_class = SongSerializer

    authentication_classes = [authentication.TokenAuthentication]

    permission_classes = [permissions.IsAuthenticated]


    