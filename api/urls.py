from django.urls import path
from . import views

urlpatterns = [
  path('notes/', views.NoteListCreate.as_view(), name='note-list'),
  path('notes/delete/<int:pk>/', views.NoteDelete.as_view(), name='note-delete'),
  path('characters/', views.CharactersView.as_view(), name='characters'),
  path('characters/<int:character_id>/', views.CharactersView.as_view(), name='character_detail'),
]