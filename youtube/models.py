from django.db import models
from django.forms import ModelForm

class Video(models.Model):
    name=models.CharField(max_length=100)
    docfile = models.FileField(upload_to = 'videos/%Y/%m/%d')
    upload_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name + ": "+str(self.docfile)


class UploadFileForm(ModelForm):
    class Meta:
        model=Video
        label='파일을 선택해주세요.'
        fields = ["name", "docfile"]
    
