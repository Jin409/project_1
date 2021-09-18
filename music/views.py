from django.shortcuts import render,get_object_or_404,redirect
from .models import Song

def home(request):
    return render(request,'home.html')

#task = recommendation을 기준으로 분류를 하고 싶음. 
def rain(request):
    songs = Song.objects.filter(recommendation="rain")
    return render(request,'rain.html',{'songs':songs})

def detail(request,id):
    song = get_object_or_404(Song,pk=id)
    return render(request,'detail.html',{'song':song})

def list(request):
    return render(request,'list.html')

def sunny(request):
    songs = Song.objects.filter(recommendation="sunny")
    return render(request,'sunny.html',{'songs':songs})

def christmas(request):
    songs = Song.objects.filter(recommendation="christmas")
    return render(request,'christmas.html',{'songs':songs})

def midnight(request):
    songs = Song.objects.filter(recommendation="midnight")
    return render(request,'midnight.html',{'songs':songs})

def create(request):
    return render(request,'create.html')

def new(request):
    post = Song()
    post.songtitle = request.POST['songtitle']
    post.songwriter = request.POST['songwriter']
    post.video = request.POST['video']
    post.recommendation = request.POST['recommendation']
    post.lyrics = request.POST['lyrics']
    post.writer = request.POST['writer']
    post.save()
    return redirect('music:detail',post.id)