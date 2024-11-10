from django import forms 
from .models import Note


class NoteForm(forms.ModelForm):
    model = Note
    fields = ('titles', 'cotent')