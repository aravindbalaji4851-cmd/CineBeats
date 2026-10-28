from django.shortcuts import render,get_object_or_404

from rest_framework import authentication,permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import RetrieveAPIView,UpdateAPIView,DestroyAPIView

from film.models import Movie

from response.models import Review
from response.serializers import ReviewSerializer
from response.permissions import IsOwner


class ReviewCreateListView(APIView):

    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def post(self,request,pk=None):

        movie_obj = get_object_or_404(Movie,id=pk)

        form_data = request.data

        serializer = ReviewSerializer(data=form_data)

        if serializer.is_valid():

            instance = serializer.save(movie=movie_obj,owner=request.user)

            serializer_inst = ReviewSerializer(instance)

            return Response(data=serializer_inst.data)

        else: return Response(data=serializer.errors)

    def get(self,request,pk=None):

        movie_obj = Movie.objects.get(id=pk)

        qs = Review.objects.filter(movie =movie_obj)

        serializer = ReviewSerializer(qs,many=True)

        return Response(data=serializer.data)


class ReviewRetrieveUpdateDeleteView(RetrieveAPIView,UpdateAPIView,DestroyAPIView):

    serializer_class = ReviewSerializer

    queryset = Review.objects.all()

    authentication_classes = [authentication.TokenAuthentication]

    permission_classes = [IsOwner]