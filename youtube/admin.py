from django.contrib import admin

from youtube.models import Video,Comment

@admin.register(Video)
class PostAdmin(admin.ModelAdmin):
    list_display = ['id','title', 'file', 'des']
    list_display_links = ['title', 'file']

    
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = (
        'video', 
        'comment_body',
        'comment_date',
    )
    search_fields = ('video__title', 'comment_body', 'comment_date',)