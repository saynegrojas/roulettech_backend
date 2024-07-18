from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# Authenticated users
# ORM --> we write out the model in Python and Django will handle converting this into correct SQL statements for us
# We define the type of fields we want to include in our model or table, and Django will map it for us
class Note(models.Model): 
  title = models.CharField(max_length=100)
  content = models.TextField()
  # auto_now_add = True --> automatically sets the field to the current date and time when the object is created
  created_at = models.DateTimeField(auto_now_add=True)
  # Foreign keys --> can link one object to another object (link user with some data that belongs to that user)
  # on_delete --> CASCADE --> will delete all the related data with that object
  author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='notes')

# self = this --> self refers to the instance of the class itself?
  def __str__(self):
    return self.title

# Likes
class Likes(models.Model):
  title = models.CharField(max_length=100)
  like = models.BooleanField(default=False)
  liked_at = models.DateTimeField(auto_now_add=True)
  author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='likes')

  def __str__(self):
    return self.title