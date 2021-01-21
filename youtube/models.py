from django.db import models
from django.utils import timezone

class Video(models.Model):
    title = models.CharField(max_length=100)
    file = models.FileField(upload_to='video/')
    des = models.CharField(max_length=1000, blank=True)

    uploaded_at = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering=('-uploaded_at',)

    def __str__ (self):
        return self.title