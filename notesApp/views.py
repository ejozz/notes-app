from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
from django.template import loader
from .models import Note, NoteForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User


def index(request):
    return redirect('/notesApp/auth/login')

def notes(request):
    notes_list = Note.objects.filter(user=request.user).order_by("dateCreated")
    template = loader.get_template('notesApp/notestest.html')
    context = { "notes_list": notes_list }
    return HttpResponse(template.render(context, request))


def note(request, note_id):
    note = Note.objects.get(id=note_id)
    template = loader.get_template('notesApp/note.html')
    context = { "note": note }
    return HttpResponse(template.render(context, request))

def noteTitle(request, note_id):
    return HttpResponse(Note.objects.get(id=note_id).title)

def noteText(request, note_id):
    return HttpResponse(Note.objects.get(id=note_id).noteText)

def listNotes(request):
    return HttpResponse(Note.objects.all().values_list('title',flat=True))

def newNote(request):
    template = loader.get_template('notesApp/newNote.html')
    context = {  }
    return HttpResponse(template.render(context,request))

def createNote(request):
    if request.method == 'POST':
        form = NoteForm(request.POST)
        if form.is_valid():
            # create a new `Band` and save it to the db
            note = form.save()
            # redirect to the detail page of the band we just created
            # we can provide the url pattern arguments as arguments to redirect function
            return redirect('note', note.id)

    else:
        form = NoteForm(initial = {'user':request.user})

    return render(request,
                'notesApp/newNote.html',
                {'form': form})

def editNote(request, note_id):
    note = Note.objects.get(id=note_id)
    if request.method == 'POST':
        form = NoteForm(request.POST, instance=note)
        if form.is_valid():
            # create a new `Band` and save it to the db
            note = form.save()
            # redirect to the detail page of the band we just created
            # we can provide the url pattern arguments as arguments to redirect function
            return redirect('note', note.id)

    else:
        form = NoteForm(initial={'title':note.title, 'noteText':note.noteText})

    template = loader.get_template('notesApp/editNote.html')
    context = { "note": note, 'form': form }
    
    return HttpResponse(template.render(context, request))

def deleteNote(request, note_id):
    Note.objects.get(id=note_id).delete()
    return redirect('notes')

def userLogin(request):
    username = request.POST["username"]
    password = request.POST["password"]
    user = authenticate(request, username=username, password=password)
    if user is not None:
        # Save session as cookie to login the user
        login(request, user)
        # Success, now let's login the user.
        return redirect('notes')
    else:
        # Incorrect credentials, let's throw an error to the screen.
        context = { 'error_message': 'Incorrect username and / or password.' }
        return render(request, context)
