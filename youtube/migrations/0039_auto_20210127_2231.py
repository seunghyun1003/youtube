# Generated by Django 3.1.5 on 2021-01-27 13:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('youtube', '0038_auto_20210127_2227'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='title',
            field=models.CharField(max_length=100, verbose_name='제목'),
        ),
    ]
