from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import UserSerializer, NoteSerializer, LikesSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny
# ????
from .models import Note, Likes
import requests

# Create Note
# ListCreateAPIView --> we use this since we are listing all the notes the user created or create a new note
class NoteListCreate(generics.ListCreateAPIView):
  serializer_class = NoteSerializer
  # [IsAuthenticated] --> is like data annotation where a user is unable to call this route if you unless the user is authenticated and pass a valid JWT token
  permission_classes = [IsAuthenticated]

  # filter all the notes that belong to the user and get a list of all the notes
  def get_queryset(self):
    user = self.request.user
    # returns all the notes that belong to the user. We can add more arguments to filter by other fields (title, content, etc.)
    return Note.objects.filter(author=user)
  
  def perform_create(self, serializer):
    # override the query_set when we pass the serializer
    if serializer.is_valid():
      serializer.save(author=self.request.user)
    else:
      print(serializer.errors)

# Delete Note
class NoteDelete(generics.DestroyAPIView):
  serializer_class = NoteSerializer
  permission_classes = [IsAuthenticated]
  def get_queryset(self):
    user = self.request.user
    return Note.objects.filter(author=user)


# Built-Django view that automatically creates a new User or object
class CreateUserView(generics.CreateAPIView):
  # queryset looks into all the objects we look into when creating a new user, and it will check if the username already exists.
  queryset = User.objects.all()
  # serailizer_class is the class that tells this view what kind of data we need to accept (ex. username and password)
  serializer_class = UserSerializer
  # permission_classes specifies who can call this view
  permission_classes = [AllowAny]


class CharactersView(APIView):
  def get(self, request, character_id=None, *args, **kwargs):
    base_url = f'https://rickandmortyapi.com/api/character'
    
    character_url = f"{base_url}/{character_id}" if character_id else base_url

    response = requests.get(character_url)

    # Checking if request was successful
    if response.status_code == 200:
      data = response.json()
      return Response(data)
    else:
      return Response({'error': 'Failed to retrieve data'}, status=response.status_code)