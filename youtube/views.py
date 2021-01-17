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


def mychannel(request):
    return render(request, 'youtube/mychannel.html')


def search(request):
    return render(request, 'youtube/search.html')


from django.template import RequestContext

"""
from .models import Video
from .forms import UploadFileForm

def form(request):
    return render(request, "youtube/form.html")
    
def mychannel(request):
    #파일 업로드
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            newdoc = Video(docfile = request.FILES['docfile'])
            newdoc.save()

            #POST가 끝나고 내 채널로 리다이렉트
            return render(request, 'youtube/mychannel.html')
    else:
        form = UploadFileForm()

    videos = Video.objects.all().order_by('-upload_date')

    return render(
        request,
        'youtube/mychannel.html',
        {'videos': videos}
    )
"""