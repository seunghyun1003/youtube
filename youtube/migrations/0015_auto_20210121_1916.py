# Generated by Django 3.1.5 on 2021-01-21 10:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('youtube', '0014_auto_20210121_1852'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='file',
            field=models.FileField(upload_to='video'),
        ),
    ]
