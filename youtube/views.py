from django.shortcuts import render

# Create your views here.

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

def mychannel(request):
    return render(request, 'youtube/mychannel_upload.html')

def mychannel_list(request):
    return render(request, 'youtube/mychannel_list.html')

def top(request):
    return render(request, 'youtube/top.html')

def search(request):
    return render(request, 'youtube/search.html')


from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.core.files.storage import FileSystemStorage
from .models import Video

def video_list(request):
    videos = Video.objects.all()
    return render(request, 'youtube/index.html', {
        'videos' : videos
    })
    
def video_list_mych(request):
    videos = Video.objects.all()
    return render(request, 'youtube/mychannel_list.html', {
        'videos' : videos
    })

def video_upload(request):
    if request.method == "POST":
        title = request.POST['title']
        video = request.POST['video']
        des = request.POST['des']
        Video.objects.create(title=title,file=video,des=des)
        return redirect('youtube:video_list_mych')
    else:
        return render(request, 'youtube/mychannel_upload.html')

    return render(request, 'youtube/mychannel_upload.html')

def video_delete(request, id):
    if request.method == "POST":
        video = Video.objects.get(pk=id)
        video.delete()
        return redirect('youtube:video_list_mych')
    return render(request, 'youtube/mychannel_list.html')


def detail_page(request, id):
    video = get_object_or_404(Video,pk=id)
    return render(request, 'youtube/video.html', {'video': video})