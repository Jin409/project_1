from django.shortcuts import render
from .models import Song

def home(request):
    return render(request,'home.html')

def song(request):
    songs = Song.objects.all()
    return render(request,'song.html',{'songs':songs})