from django.contrib import admin

from .models import VideoModel

@admin.register(VideoModel)
class VideoAdmin(admin.ModelAdmin):
    list_display = ('id','videoname', 'uploaded_at', 'des')
    list_filter = ('uploaded_at',)
    search_fields = ('videoname',)