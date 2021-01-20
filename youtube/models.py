from django.db import models

class Video(models.Model):
    title = models.CharField(max_length=100)
    file = models.FileField(upload_to='video')
    des = models.CharField(max_length=1000)

    def __str__ (self):
        return self.title