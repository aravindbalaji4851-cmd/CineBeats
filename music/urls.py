from django.urls import path
from music.views import SongListCreateView,SongRetrieveUpdateDestroyView

urlpatterns = [
    path('songs/', SongListCreateView.as_view()),
    path('<int:pk>/', SongRetrieveUpdateDestroyView.as_view()),
]