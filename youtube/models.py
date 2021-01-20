from django.db import models
from django.utils import timezone

class VideoModel(models.Model):
    videoname = models.CharField(max_length=200, null=False)
    uploaded_at = models.DateTimeField('업로드 날짜', default = timezone.now)
    videofile = models.FileField(upload_to="video/", null=False)
    des = models.TextField('동영상 설명',null=True)

    def __str__(self):
        return self.videoname

    def summary(self):
        return self.des
