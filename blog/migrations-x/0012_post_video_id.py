# Generated by Django 4.0.4 on 2022-06-08 13:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0011_remove_post_video_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='video_id',
            field=models.CharField(blank=True, default='dQw4w9WgXcQ', max_length=15),
        ),
    ]
