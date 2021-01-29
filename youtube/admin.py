from django.contrib import admin
from youtube.models import Video,Comment


class VideoAdmin(admin.ModelAdmin):
    list_display = ['id', 'writer','title','des']
    search_fields = ('title', 'des')

admin.site.register(Video, VideoAdmin)
    
class CommentAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'video', 
        'commenter',
        'comment_body',
        'comment_date',
    )
    search_fields = ('video__title', 'comment_body', 'commenter',)

admin.site.register(Comment, CommentAdmin)