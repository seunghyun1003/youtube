from django.urls import path
from . import views

app_name = 'youtube_backend'

urlpatterns = [
    path('', views.video_list, name='video_list'),
    path('index', views.video_list, name='video_list'),
    path('<int:id>', views.detail_page, name='detail'),
    path('login/', views.login, name='login'),
    path("logout", views.logout_request, name="logout"),
    path('who', views.who, name='who'),
    path('search', views.search, name='search'),
    path('video', views.video, name='video'),
    path('top', views.top, name='top'),
    path('mychannel', views.video_upload_form, name="video_upload_form"),
    path('search', views.search, name='search'),
]
