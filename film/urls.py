
from django.urls import path

from film.views import MovieListCreateView,MovieRetrieveUpdateDeleteView

urlpatterns = [
    path('', MovieListCreateView.as_view()),
    path("<int:pk>/",MovieRetrieveUpdateDeleteView.as_view()),
]

