from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework  import authentication,permissions
from rest_framework.generics import RetrieveUpdateDestroyAPIView

from film.models import Movie
from film.serializers import MovieSerializer


class MovieListCreateView(APIView):

    authentication_classes = [authentication.TokenAuthentication]

    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):

        movies = Movie.objects.all()

        serializer = MovieSerializer(movies, many=True)

        return Response(data=serializer.data)

    def post(self, request):

        form_data = request.data

        serializer = MovieSerializer(data=form_data)

        if serializer.is_valid():

            serializer.save(created_by=request.user)
            
            return Response(data=serializer.data)

        return Response(data=serializer.errors)

class MovieRetrieveUpdateDeleteView(RetrieveUpdateDestroyAPIView):

    queryset = Movie.objects.all()

    serializer_class = MovieSerializer

    authentication_classes = [authentication.TokenAuthentication]

    permission_classes = [permissions.IsAuthenticated]

