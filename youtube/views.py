from django.shortcuts import render

# Create your views here.

from social_core.exceptions import AuthAlreadyAssociated
from django.shortcuts import redirect
from django.http import HttpResponse


from .models import Video
from django.db.models import Q

def search(request):
    return render(request, 'youtube/search.html')

def search_result(request):
    videos = Video.objects.order_by('-hits').all()
    query = None

    if 'q' in request.GET:
        query = request.GET.get('q','')
        videos = videos.filter(
                Q(title__icontains=query) | 
                Q(des__icontains=query) | 
                Q(writer__icontains=query)
        )
        return redirect('youtube:search')
        return render(request, 'youtube/search.html',{
            'query':query,
            'videos':videos
        })

from .forms import UserForm, LoginForm
from django.contrib.auth import login, logout , authenticate
from django.template import RequestContext

from django.contrib.auth import get_user_model

User = get_user_model()

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
from django.utils import timezone
from django.contrib import messages

#모든 게시물 가져오기
def video_list(request):
    videos = Video.objects.all()
    return render(request, 'youtube/index.html', {
        'videos' : videos
    })
    
#사용자별 게시물 가져오기
def video_list_mych(request):
    user = request.user
    videos = Video.objects.filter(writer = user).order_by('-uploaded_at')
    return render(request, 'youtube/mychannel_list.html',{
        'videos' : videos
    })

#비디오 업로드
def video_upload(request):
    if request.method == "POST":
        title = request.POST['title']
        video = request.FILES['videofile']
        des = request.POST['des']
        writer = request.user
        content = Video(title=title,file=video,des=des,writer=writer)
        content.save()
        return redirect('youtube:video_list_mych')
    else:
        return render(request, 'youtube/mychannel_upload.html')

#비디오 수정
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

#비디오 삭제
def video_delete(request, id):
    if request.method == "POST":
        video = Video.objects.get(pk=id)
        video.delete()
    return redirect('youtube:video_list_mych')

#비디오 디텡일 페이지
def detail_page(request, id):
    video = get_object_or_404(Video,pk=id)
    comments = Comment.objects.all()
    if comments.exists():
        comments.order_by('-comment_date')
        return render(request, 'youtube/video.html', {
            'comments':comments,
            'video': video
        })
    else:
        return render(request, 'youtube/video.html', {
            'video': video
        })

#인기순으로 비디오 정렬
def top(request):
    videos = Video.objects.all().order_by('-hits')
    return render(request, 'youtube/top.html', {
        'videos' : videos
    })

from .models import Comment

def comment_write(request, id):
    if request.method == "POST":
        video = get_object_or_404(Video,pk=id)
        comment_body = request.POST['comment']
        commenter = request.user
        comment = Comment(video=video,commenter=commenter,comment_body=comment_body)
        comment.save()
        return redirect('youtube:detail',id)
    else:
        return render(request, 'youtube/video.html',{
            'video': video,
        })

#댓글 삭제
def comment_delete(request, video_id, comment_id):
    video = get_object_or_404(Video,pk=video_id)
    comment = get_object_or_404(Comment, id=comment_id)
    if comment.commenter == request.user:
        comment.delete()
        return redirect('youtube:detail',video_id)
    return render(request, 'youtube/video.html', {
        'video': video,
        'comment':comment,
    })

