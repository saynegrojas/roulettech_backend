from django.db import models
from django.contrib.auth.models import User

# Likes
class Likes(models.Model):
  title = models.CharField(max_length=100)
  like = models.BooleanField(default=False)
  liked_at = models.DateTimeField(auto_now_add=True)
  author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='likes')

  def __str__(self):
    return self.title