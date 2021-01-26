from django.shortcuts import render

# Create your views here.

from social_core.exceptions import AuthAlreadyAssociated
from django.shortcuts import redirect
from django.http import HttpResponse

def mychannel(request):
    return render(request, 'youtube/mychannel_upload.html')

def mychannel_list(request):
    return render(request, 'youtube/mychannel_list.html')

def search(request):
    return render(request, 'youtube/search.html')

from django.contrib.auth.models import User
from .forms import UserForm, LoginForm
from django.contrib.auth import login, logout , authenticate
from django.template import RequestContext


def signup(request):  
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            new_user = User.objects.create_user(**form.cleaned_data)
            login(request, new_user)
            return redirect('youtube:video_list')
    else:
        form = UserForm()
        return render(request, 'youtube/signup.html', {'form': form})


def signin(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username = username, password = password)
        if user is not None:
            login(request, user)
            return redirect('youtube:video_list')
        else:
            return HttpResponse('로그인 실패. 다시 시도 해보세요.')
    else:
        form = LoginForm()
        return render(request, 'youtube/login.html', {'form': form})

    
    
def signout(request):
    logout(request)
    return redirect('youtube:video_list')

def who(request):
    user_pk = request.session.get('user') #login함수에서 추가한 request.session['user'] = user.id 
    if user_pk:
        user = User.objects.get(pk=user_pk)
        return render(request, 'youtube/who.html', {
            'user' : user
        })
    return render(request, 'youtube/who.html')


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

def top(request):
    videos = Video.objects.all().order_by('-hits')
    return render(request, 'youtube/top.html', {
        'videos' : videos
    })


import json
from django.core import serializers
from django.core.serializers.json import DjangoJSONEncoder

def comment_write(request, id):
    video = get_object_or_404(Video,pk=id)
    comment_body = request.POST['comment']
    comment  = Comment.objects.create(video=video, comment_body=comment_body)
    video.save()
    data = {
        'comment_body' : comment_body,
        'comment_date' : '방금 전',
        'comment_id' : comment.id
    }
    return HttpResponse(json.dumps(data, cls=DjangoJSONEncoder), content_type = "application/json")

def comment_delete(request, id):
    video = get_object_or_404(Video,pk=id)
    video.save()
    data = {
        'comment_id': comment_id,
    }
    return HttpResponse(json.dumps(data, cls=DjangoJSONEncoder), content_type = "application/json")