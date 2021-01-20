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


from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.core.files.storage import FileSystemStorage

from .models import Video

def video_upload_form(request):
    if request.method == "POST":
        title = request.POST['title']
        video = request.POST['video']
        video_key = request.POST['video_key']
        des = request.POST['des']
        content = Video(title=title,file=video,des=des,video_key = video_key)
        content.save()
        
    videos = Video.objects.all()
    return render(request, 'youtube/mychannel.html', {
        'videos' : videos
    })

def video_list(request):
    videos = Video.objects.all()
    return render(request, 'youtube/index.html', {
        'videos' : videos
    })

def detail_page(request, id):
    video = get_object_or_404(Video,pk=id)
    return render(request, 'youtube/video.html', {'video': video})