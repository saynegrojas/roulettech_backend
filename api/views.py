from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import UserSerializer
from rest_framework.permissions import AllowAny
import requests


# Built-Django view that automatically creates a new User or object
class CreateUserView(generics.CreateAPIView):
  queryset = User.objects.all()
  serializer_class = UserSerializer
  permission_classes = [AllowAny]

class CharactersView(APIView):
  def get(self, request, character_id=None, *args, **kwargs):
    if character_id:
        url = f'https://rickandmortyapi.com/api/character/{character_id}'
    else:
        url = f'https://rickandmortyapi.com/api/character'

    response = requests.get(url)

    if response.status_code == 200:
      data = response.json()
      return Response(data)
    else:
      return Response({'error': 'Failed to retrieve data'}, status=response.status_code)