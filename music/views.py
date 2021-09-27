from django.shortcuts import render,get_object_or_404,redirect
from .models import Song
from .models import Comment

def home(request):
    return render(request,'home.html')

#task = recommendation을 기준으로 분류를 하고 싶음. 
def rain(request):
    songs = Song.objects.filter(recommendation="rain")
    return render(request,'rain.html',{'songs':songs})

def detail(request,id):
    song = get_object_or_404(Song,pk=id)
    comments = Comment.objects.filter(post=song)

    if request.method=="POST":
        new_comment = Comment()
        new_comment.post = song
        new_comment.name = request.POST['name']
        new_comment.text = request.POST['text']
        new_comment.opinion = request.POST['opnion']
        new_comment.save()
    return render(request,'detail.html',{'song':song,'comments':comments})

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

def delete(request,id):
    song = Song.objects.get(pk=id)
    song.delete()
    return redirect('home')

def comment_delete(request,id):
    comment = Comment.objects.get(pk=id)
    comment.delete()
    return redirect('music:detail',comment.post_id)

def find(request):
    songs = Song.objects.all()
    find = request.GET.get('find')
    srtfind = find[0:2]
    return render(request,'find.html',{'songs':songs,'find':find,'srtfind':srtfind})



