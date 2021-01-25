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

def search(request):
    return render(request, 'youtube/search.html')


from django.shortcuts import render, redirect, get_object_or_404
from django.core.files.storage import FileSystemStorage
from .models import Video, Comment
from django.utils import timezone

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
        video = request.FILES['videofile']
        des = request.POST['des']
        content = Video(title=title,file=video,des=des)
        content.save()
        return redirect('youtube:video_list_mych')
    else:
        return render(request, 'youtube/mychannel_upload.html')

    return render(request, 'youtube/mychannel_upload.html')

def video_update(request, id):
    video = Video.objects.get(pk=id)
    if request.method == "POST":
        video.title = request.POST['title']
        video.des = request.POST['des']
        video.uploaded_at = timezone.datetime.now()
        video.save()
        return redirect('youtube:video_list_mych')
    else:
        return render(request, 'youtube/video_update.html',{'video': video,})
    return render(request, 'youtube/video_update.html',{'video': video,})

def video_delete(request, id):
    if request.method == "POST":
        video = Video.objects.get(pk=id)
        video.delete()
    return redirect('youtube:video_list_mych')

def detail_page(request, id):
    video = get_object_or_404(Video,pk=id)
    if request.method == "POST":
        comment_body = request.POST['comment']
        comments = Comment(video=video, comment_body=comment_body)
        comments.save()
        return render(request, 'youtube/video.html', {
            'video': video,
            'comments' : comments
            })
    return render(request, 'youtube/video.html', {'video': video})

def comment_write(request, id):
    video = get_object_or_404(Video,pk=id)
        

def top(request):
    videos = Video.objects.all().order_by('-hits')
    return render(request, 'youtube/top.html', {
        'videos' : videos
    })
