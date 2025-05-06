from django.shortcuts import render, redirect, get_object_or_404
from .models import Note



# Views for the Note application

def welcome(request):
    return render(request, "welcome.html")
def index(request):
    """
    Display the list of notes and handle the creation of a new note.
    """
    notes = Note.objects.all()
    if request.method == 'POST':
        text = request.POST.get('note', '').strip()
        if text:  # Ensure the note text is not empty
            Note.objects.create(text=text)
        return redirect('index')
    return render(request, 'index.html', {'notes': notes})


def delete_note(request, id):
    """
    Delete a specific note by its ID.
    """
    note = get_object_or_404(Note, id=id)
    note.delete()
    return redirect('index')


def edit_note(request, id):
    """
    Edit an existing note by its ID.
    """
    note = get_object_or_404(Note, id=id)
    if request.method == 'POST':
        updated_text = request.POST.get('note', '').strip()
        if updated_text:  # Ensure the updated text is not empty
            note.text = updated_text
            note.save()
        return redirect('index')
    return render(request, 'edit.html', {'note': note})