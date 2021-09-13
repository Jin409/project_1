from django.shortcuts import render

def home(request):
    return render(request,'home.html')

def song(request):
    return render(request,'song.html')