from django.urls import path

from response.views import ReviewCreateListView,ReviewRetrieveUpdateDeleteView

urlpatterns = [
    path("movies/<int:pk>/review/",ReviewCreateListView.as_view()),
    path("review/<int:pk>/",ReviewRetrieveUpdateDeleteView.as_view())
]