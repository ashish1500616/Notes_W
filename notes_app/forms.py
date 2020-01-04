from django import forms
from .models import Note ,Tag

class NoteForm(forms.ModelForm):
    class Meta:
        model=Note
        fields='__all__'