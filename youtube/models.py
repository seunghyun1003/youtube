from django.db import models
from django.utils import timezone
from django.contrib.auth import get_user_model

class Video(models.Model):
    title = models.CharField(max_length=100, verbose_name = "제목")
    file = models.FileField(upload_to='video/', verbose_name = "동영상")
    des = models.TextField(max_length=1000, verbose_name = "설명")
    writer = models.ForeignKey(get_user_model(), verbose_name = "게시자", on_delete = models.CASCADE, blank=True, null=True)
    uploaded_at = models.DateTimeField(default=timezone.now)
    
    hits = models.PositiveIntegerField(default = 0)
    like_users = models.ManyToManyField(get_user_model(), related_name="like_videos", blank=True)
    dislike_users = models.ManyToManyField(get_user_model(), related_name="dislike_videos", blank=True)

    class Meta:
        ordering=('-uploaded_at',)

    def __str__ (self):
        return self.title
        
    @property
    def click(self):
        self.hits = self.hits + 1
        self.save()

class Comment(models.Model):
    commenter = models.ForeignKey(get_user_model(), verbose_name = "작성자", on_delete = models.CASCADE, blank=True, null=True)
    video = models.ForeignKey(Video, related_name='comments', on_delete=models.CASCADE)
    comment_date = models.DateTimeField(auto_now_add=True)
    comment_body = models.TextField(max_length=1000)

    class Meta:
        ordering=('-comment_date',)


