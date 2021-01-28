from django.contrib import admin
from youtube.models import Video,Comment


class VideoAdmin(admin.ModelAdmin):
    list_display = ['id','title', 'writer']
    search_fields = ('title', 'writer')

admin.site.register(Video, VideoAdmin)
    
class CommentAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'video', 
        'commenter',
        'comment_body',
        'comment_date',
    )

admin.site.register(Comment, CommentAdmin)