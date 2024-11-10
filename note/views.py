from django.shortcuts import render, redirect
from .models import Note
from .forms import NoteForm

# Create your views here.

def home(request):
    notes = Note.objects.all()
    return render(request, 'home.html', {'notes': notes})

def newnotes(request):
    return render(request, 'newnotes.html')

def notes(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        note = Note(title=title, content=content)
        note.save()
        return redirect(home)
    return redirect(home)

def edit(request, id):
    note = Note.objects.get(id=id)
    return render(request, 'edit.html', {'note': note})

def updateNote(request):
    if request.method == 'POST':
        if request.POST.get('update'):
            id = request.POST.get('update')
            note = Note.objects.get(id=id)
            note.title = request.POST.get('title')
            note.content = request.POST.get('content')            
            note.save()
        elif request.POST.get('delete') :
            id = request.POST.get('delete')
            note = Note.objects.get(id=id)   
            note.delete()    

        return redirect(home)
    return redirect(home)
    
