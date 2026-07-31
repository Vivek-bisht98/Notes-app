from django.shortcuts import render,redirect
from .models import Note

# Create your views here.
def home(request):
    notes=Note.objects.all()
    return render(request,'home.html',{'notes':notes})

def create(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        note = Note(title=title, content=content)
        note.save()
        return redirect('home')
    return render(request,'create_note.html')

def edit(request,id):
    note = Note.objects.get(id=id)
    if request.method == 'POST':
        note.title = request.POST.get('title')
        note.content = request.POST.get('content')
        note.save()
        return redirect('home')
    return render(request,'edit_note.html',{'note':note})

def view_note(request,id):
    note = Note.objects.get(id=id)
    return render(request,'view_note.html',{'note':note})

def delete_note(request,id):
    note = Note.objects.get(id=id)
    note.delete()
    return redirect('home')
