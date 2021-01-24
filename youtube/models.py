from django.db import models
from django.utils import timezone

class Video(models.Model):
    title = models.CharField(max_length=100)
    file = models.FileField(upload_to='video/')
    des = models.TextField(max_length=1000)
    hits = models.PositiveIntegerField(default = 0)

    uploaded_at = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering=('-uploaded_at',)

    def __str__ (self):
        return self.title
        
    @property
    def click(self):
        self.hits +=1
        self.save()