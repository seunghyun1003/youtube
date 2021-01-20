from django.contrib import admin

from youtube.models import Video

@admin.register(Video)
class PostAdmin(admin.ModelAdmin):
    list_display = ['id','title', 'file', 'des']
    list_display_links = ['title', 'file']