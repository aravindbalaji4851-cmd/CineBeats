from django.urls import path

from rest_framework.authtoken.views import ObtainAuthToken

from account.views import SignUpView


urlpatterns = [
    path('signup/',SignUpView.as_view()),
    path('token/',ObtainAuthToken.as_view()),
]