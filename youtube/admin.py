from django.contrib import admin
from youtube.models import Video,Comment


@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    list_display = ['id','title', 'writer']
    
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = (
        'video', 
        'commenter',
        'comment_body',
        'comment_date',
    )
    search_fields = ('video__title', 'commenter','comment_body', 'comment_date',)