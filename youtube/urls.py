from django.urls import path
from . import views

app_name = 'youtube_backend'

urlpatterns = [
    path('', views.video_list, name='video_list'),
    path('index', views.video_list, name='video_list'),

    path('signup', views.signup, name='signup'),
    path('login', views.signin, name='login'),
    path('logout', views.signout, name='logout'),
    path('accountinfo', views.who, name='who'),
    path('accountmod', views.account_mod, name='account_mod'),
    path('accountdel', views.account_de, name='account_de'),
    
    path('mychannel', views.video_upload, name='video_upload'),
    path('list', views.video_list_mych, name='video_list_mych'),

    path('video<int:id>', views.detail_page, name='detail'),
    path('delete<int:id>', views.video_delete, name='video_delete'),
    path('edit<int:id>', views.video_update, name='video_update'),
    path('video<int:id>/comment/write', views.comment_write, name='comment_write'),
    path('video<int:video_id>/comment/<int:comment_id>/delete', views.comment_delete, name='comment_delete'),

    path('search', views.search, name='search'),
    path('searchresult', views.search_result, name='search_result'),
    path('top', views.top, name='top'),
]
