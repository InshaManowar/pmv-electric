# Generated by Django 3.2.9 on 2021-11-19 09:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_rename_video_video_video_link'),
    ]

    operations = [
        migrations.AddField(
            model_name='photos',
            name='video_url',
            field=models.TextField(blank=True, default=None, null=True),
        ),
    ]