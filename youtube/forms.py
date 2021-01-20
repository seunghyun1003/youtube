from django.forms import ModelForm
from .models import VideoModel

class VideoUploadForm(ModelForm):
    class Meta:
        model = VideoModel
        fields = ('videoname', 'videofile',)