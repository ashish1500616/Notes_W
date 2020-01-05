from django.shortcuts import render,redirect
from .models import Note
from .forms import NoteForm
# Create your views here.
def home(request):
    all_n=Note.objects.all()
    if request.method == "POST":
        form =NoteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('notes_app:home')
    else:
        form = NoteForm()
    return render(request,'notes_app/home.html',{"notes_data_from_db":all_n,"note_form":form})


def edit(request,id):
    note_id=Note.objects.get(id=id)
    return render(request,'notes_app/edit.html',{"note":note_id})




