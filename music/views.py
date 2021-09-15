from django.shortcuts import render,get_object_or_404
from .models import Song

def home(request):
    return render(request,'home.html')

def song(request):
    songs = Song.objects.all()
    if songs == "rain":
        songs = songs
    return render(request,'song.html',{'songs':songs})

def detail(request,id):
    song = get_object_or_404(Song,pk=id)
    return render(request,'detail.html',{'song':song})