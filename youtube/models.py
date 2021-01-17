from django.db import models

class Video(models.Model):
    name = models.CharField(max_length=100)
    docfile = models.FileField(upload_to = 'videos/')
    upload_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
