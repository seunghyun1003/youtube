# Generated by Django 3.1.5 on 2021-01-21 09:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('youtube', '0013_auto_20210120_2302'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='file',
            field=models.FileField(upload_to='videos/'),
        ),
    ]
