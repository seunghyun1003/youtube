from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from social_core.exceptions import AuthAlreadyAssociated


def login(request):
    return render(request, 'youtube/login.html')

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

    
