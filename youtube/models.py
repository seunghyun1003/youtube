from django.db import models
from django.utils import timezone

class Video(models.Model):
    title = models.CharField(max_length=100)
    file = models.FileField(upload_to='video/')
    des = models.TextField(max_length=1000)

    uploaded_at = models.DateTimeField(default=timezone.now)
    
    hits = models.PositiveIntegerField(default = 0)

    class Meta:
        ordering=('-uploaded_at',)

    def __str__ (self):
        return self.title
        
    @property
    def click(self):
        self.hits = self.hits + 1
        self.save()

class Comment(models.Model):
    video = models.name = models.ForeignKey('Video', related_name='comments', on_delete=models.CASCADE)
    comment_date = models.DateTimeField(auto_now_add=True)
    comment_body = models.TextField(max_length=1000)

    class Meta:
        ordering=('-comment_date',)