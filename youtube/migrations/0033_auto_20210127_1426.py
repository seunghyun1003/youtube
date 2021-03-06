# Generated by Django 3.1.5 on 2021-01-27 05:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('youtube', '0032_delete_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='writer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='작성자'),
        ),
        migrations.AlterField(
            model_name='video',
            name='des',
            field=models.TextField(max_length=1000, verbose_name='설명'),
        ),
        migrations.AlterField(
            model_name='video',
            name='file',
            field=models.FileField(upload_to='video/', verbose_name='동영상'),
        ),
        migrations.AlterField(
            model_name='video',
            name='title',
            field=models.CharField(max_length=100, verbose_name='제목'),
        ),
    ]
