from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.core.validators import URLValidator
from django.urls import reverse
from ckeditor.fields import RichTextField
from embed_video.fields import EmbedVideoField


class ParentCategory(models.Model):
    name = models.CharField(max_length=100)
    description=RichTextField(blank=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Parent Category"
        verbose_name_plural = "Parent Categories"
class Category(models.Model):
    name = models.CharField(max_length=100)
    parent_category=models.ForeignKey('ParentCategory', on_delete=models.CASCADE, blank=True, null=True)
    description=RichTextField(blank=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"
class post(models.Model):
    title = models.CharField(max_length=100)
    content = RichTextField()
    category =models.ForeignKey('Category',null=True, blank=True, on_delete=models.CASCADE)
    excerpt = models.TextField(max_length=400, blank=True)
    embed=models.CharField(max_length=800, blank=True)
    image=models.ImageField(upload_to='blog/images', blank=True)
    video = EmbedVideoField(max_length=140, default="paste your embeded code here")
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Post"
        verbose_name_plural = "Posts"

    def get_absolute_url(self):
        return reverse("post-detail", kwargs={"pk": self.pk})
    

class Course(models.Model):
    title = models.CharField(max_length=100, verbose_name="Title")
    excerpt=models.TextField(max_length=400, blank=True)
    intro_content = RichTextField(verbose_name="Intro Content")
    detail_content = RichTextField(verbose_name="Detail Content")
    hero_img = models.ImageField(upload_to='blog/images', verbose_name="Hero Image")
    featured_img = models.ImageField(upload_to='blog/images', verbose_name="Featured Image")
    date_created=models.DateTimeField(default=timezone.now)
    
    
    def __str__(self) -> str:
        return self.title
    
    