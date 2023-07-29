from django.contrib import admin
from django.urls import include, path
from django.shortcuts import redirect

urlpatterns = [
    path('notesApp/', include('notesApp.urls')),
    path('admin/', admin.site.urls),
    path('', lambda req: redirect('/notesApp/'))
]