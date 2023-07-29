from django.urls import path
from django.conf.urls import include
from django.contrib.auth.models import User

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('auth/', include('django.contrib.auth.urls')),
    path('notes/', views.notes, name='notes'),
    path("noteTitle/<int:note_id>/", views.noteTitle, name="noteTitle"),
    path("noteText/<int:note_id>/", views.noteText, name="noteText"),
    path("note/<int:note_id>/", views.note, name="note"),
    path("listNotes/", views.listNotes, name="listNotes"),
    path("note/new/", views.createNote, name="createNote"),
    path("note/edit/<int:note_id>/", views.editNote, name="editNote"),
    path("note/delete/<int:note_id>/", views.deleteNote, name="deleteNote"),
]