from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.contrib.auth.models import User

from rest_framework.views import APIView
from rest_framework.response import Response

from account.serializers import UserSerializer

class SignUpView(APIView):

    def post(self,request):

        form_data = request.data

        serializer = UserSerializer(data=form_data)

        if serializer.is_valid():

            cleaned_data = serializer.validated_data
            
            instance = User.objects.create_superuser(**cleaned_data)

            serializer_obj = UserSerializer(instance)

            return Response(data=serializer_obj.data)

        else: return Response(data=serializer.errors)

        