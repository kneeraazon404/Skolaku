# Generated by Django 4.0.4 on 2022-05-21 17:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='slug',
            field=models.SlugField(default='karki', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='course',
            name='slug',
            field=models.SlugField(default='karki', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='parentcategory',
            name='slug',
            field=models.SlugField(default='slug', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='slug',
            field=models.SlugField(default='karki', max_length=100),
            preserve_default=False,
        ),
    ]