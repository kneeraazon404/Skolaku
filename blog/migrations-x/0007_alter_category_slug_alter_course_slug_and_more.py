# Generated by Django 4.0.4 on 2022-05-21 18:28

import autoslug.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_alter_category_slug_alter_course_slug_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='slug',
            field=autoslug.fields.AutoSlugField(blank=True, default=None, editable=False, null=True, populate_from='name', unique=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='slug',
            field=autoslug.fields.AutoSlugField(blank=True, default=None, editable=False, null=True, populate_from='title', unique=True),
        ),
        migrations.AlterField(
            model_name='parentcategory',
            name='slug',
            field=autoslug.fields.AutoSlugField(blank=True, default=None, editable=False, null=True, populate_from='name', unique=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='slug',
            field=autoslug.fields.AutoSlugField(blank=True, default=None, editable=False, null=True, populate_from='title', unique=True),
        ),
    ]