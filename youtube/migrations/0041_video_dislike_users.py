# Generated by Django 3.1.5 on 2021-02-01 13:42

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('youtube', '0040_video_like_users'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='dislike_users',
            field=models.ManyToManyField(blank=True, related_name='dislike_videos', to=settings.AUTH_USER_MODEL),
        ),
    ]
