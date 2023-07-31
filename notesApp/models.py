import datetime
from django import forms
from django.db import models
from django.utils import timezone
from django.forms import ModelForm
from django.conf import settings
from django.http import HttpRequest

from django.contrib.auth.models import User

class Note(models.Model):
    title = models.CharField(max_length=80)
    noteText = models.TextField()
    dateCreated = models.DateTimeField(auto_now_add=True)
    dateModified =  models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.title + ": " + self.noteText

class NoteForm(ModelForm):
    class Meta:    
        model = Note
        fields = ['user', 'title','noteText']
        widgets = {'user': forms.HiddenInput()}

        

# class RegisterForm(UserCreationForm):
#     class Meta:
#         model = User
#         fields = ["user", "password"]