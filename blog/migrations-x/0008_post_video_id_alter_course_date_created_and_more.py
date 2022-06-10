# Generated by Django 4.0.4 on 2022-06-08 12:57

from django.db import migrations, models
import django.utils.timezone
import embed_video.fields


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_alter_category_slug_alter_course_slug_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='video_id',
            field=models.CharField(blank=True, max_length=15),
        ),
        migrations.AlterField(
            model_name='course',
            name='date_created',
            field=models.DateTimeField(default=django.utils.timezone.now, editable=False),
        ),
        migrations.AlterField(
            model_name='post',
            name='video',
            field=embed_video.fields.EmbedVideoField(blank=True, default='', editable=False, max_length=140),
        ),
    ]
