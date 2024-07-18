from django.contrib.auth.models import User
from rest_framework import serializers

from .models import Note
from .models import Likes

# Serializers --> a component of the Django REST Framework (DRF) that allows you to convert complex data types, such as Django models or querysets, into Python data types that can be easily rendered into formats like JSON or XML. 
# Serializers also handle the deserialization process, which converts incoming data from formats like JSON or XML into Python data types that can be used to create or update Django model instances.

# ORM Creating a serializer in Django allows for converting Python objects to JSON data for communication with web applications. Serializers help in handling database operations automatically.
# Accepting json with username and password & returning json data with user details as a response

class UserSerializer(serializers.ModelSerializer):
  # class Meta --> is a nested class inside a model or serializer class that allows you to define metadata or options for that class.
  class Meta:
    model = User
    # Fields we want to serialize when we are accepting and returning data
    fields = ['id', 'username', 'password']
    #  This `extra_kwargs` setting is used to mark the `password` field as `write_only`, which means it will be accepted as input during serialization, but will not be included in the serialized output. This is a common security practice to avoid exposing sensitive user information in the API response.
    extra_kwargs = {'password': {'write_only': True}}

# Creates a new user instance with the provided validated data and returns the created user.?
# Args --> validated_data (dict): A dictionary containing the validated user data, such as username and password.
# Returns: --> User: The newly created user instance.?
  def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user
  
  
# Now that we have a"Notes" "model created, we need to create a serializer for it since it's an API, we need to convert it to JSON data so that we can receive and return it
class NoteSerializer(serializers.ModelSerializer):
   class Meta:
      model = Note
      fields = ['id', 'title', 'content', 'created_at', 'author']
      # This `extra_kwargs` setting is used to mark the `author` field as `read_only`, which means it will be accepted as input during serialization, but will not be included in the serialized output.
      extra_kwargs = {'author': {'read_only': True}}

# Likes Serializer
class LikesSerializer(serializers.ModelSerializer):
   class Meta:
      model = Likes
      fields = ['id', 'title', 'like', 'liked_at', 'author']
      extra_kwargs = {'author': {'read_only': True}}