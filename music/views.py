from django.shortcuts import render,get_object_or_404
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