from django.urls import path
from . import views

app_name = 'youtube_backend'

urlpatterns = [
    path('', views.video_list, name='video_list'),
    path('index', views.video_list, name='video_list'),
    path('mychannel', views.video_upload, name='video_upload'),
    path('list', views.video_list_mych, name='video_list_mych'),
    path('<int:id>', views.detail_page, name='detail'),
    path('<int:id>/delete', views.video_delete, name='video_delete'),
    path('<int:id>/edit', views.video_update, name='video_update'),
    path('login/', views.login, name='login'),
    path("logout", views.logout_request, name="logout"),
    path('who', views.who, name='who'),
    path('search', views.search, name='search'),
    path('top', views.top, name='top'),
]
