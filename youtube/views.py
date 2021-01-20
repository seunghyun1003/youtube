from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from social_core.exceptions import AuthAlreadyAssociated
from django.contrib.auth import logout
from django.shortcuts import redirect

def login(request):
    return render(request, 'youtube/login.html')

def logout_request(request):
    logout(request)
    return render(request, 'youtube/index.html', {'name': index,})

def who(request):
    return render(request, 'youtube/who.html')

def index(request):
    return render(request, 'youtube/index.html')

def video(request):
    return render(request, 'youtube/video.html')


def top(request):
    return render(request, 'youtube/top.html')

def search(request):
    return render(request, 'youtube/search.html')


from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core.files.storage import FileSystemStorage

from .forms import VideoForm
from .models import Video

def video_upload_form(request):
    if request.method == "POST":
        form = VideoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    else:
        form = VideoForm()
        
    videos = Video.objects.all()
    return render(request, 'youtube/mychannel.html', {
        'form' : form, 
        'videos' : videos
    })

def video_list(request):
    videos = Video.objects.all()
    return render(request, 'youtube/index.html', {
        'videos' : videos
    })
