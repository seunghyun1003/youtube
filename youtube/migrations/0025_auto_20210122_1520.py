# Generated by Django 3.1.5 on 2021-01-22 06:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('youtube', '0024_auto_20210122_1502'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='des',
            field=models.TextField(max_length=1000),
        ),
    ]