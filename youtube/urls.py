from django.urls import path
from . import views

app_name = 'youtube_backend'

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login, name='login'),
    path('who', views.who, name='who'),
    path('search', views.search, name='search'),
    path('index', views.index, name='index'),
    path('video', views.video, name='video'),
    path('top', views.top, name='top'),
    path('mychannel', views.mychannel, name='mychannel'),
    path('search', views.search, name='search'),
]