
from django.db import models
from embed_video.fields import EmbedVideoField

# Create your models here.
class General(models.Model):
    name=models.CharField(max_length=100)
    logo=models.ImageField(upload_to='images/', blank=True, null=True)
    favicon=models.ImageField(upload_to='images/', blank=True, null=True)
    whatsapp_no=models.CharField(max_length=20, blank=True, null=True)
    def __str__(self):
        return self.name
    
class HomePage(models.Model):
    title=models.CharField(max_length=100)
    excerpt=models.TextField(blank=True, null=True)
    hero_img=models.ImageField(upload_to='images/', blank=True, null=True)
    featured_img=models.ImageField(upload_to='images/', blank=True, null=True)
    home_product_title=models.CharField(max_length=100,verbose_name='Home Product Title')
    card_image=models.ImageField(upload_to='images/', blank=True, null=True)
    card_title=models.CharField(max_length=100)
    card_desc=models.TextField(blank=True, null=True)

    def __str__(self):
        return self.title
    
class USP(models.Model):
    title=models.CharField(max_length=100)
    card_title=models.CharField(max_length=100)
    card_img=models.ImageField(upload_to='images/', blank=True, null=True)
    carad_desc=models.TextField(blank=True, null=True)
    
    def __str__(self):
        return self.title
    

class Testimonials(models.Model):
    title=models.CharField(max_length=100)
    image=models.ImageField(upload_to='images/', blank=True, null=True)
    video = EmbedVideoField(max_length=140, default="", blank=True)
    description=models.TextField(blank=True, null=True)
    
    def __str__(self):
        return self.title
    
    
class Bonus(models.Model):
    title=models.CharField(max_length=100)
    card_title=models.CharField(max_length=100)
    image=models.ImageField(upload_to='images/', blank=True, null=True)
    
    def __str__(self):
        return self.title
    
class Trainer(models.Model):
    title=models.CharField(max_length=100)
    image=models.ImageField(upload_to='images/', blank=True, null=True)
    name=models.CharField(max_length=100)
    occupation=models.CharField(max_length=100)
    linkedin=models.URLField(max_length=100, blank=True, null=True)
    
    def __str__(self):
        return self.title
class Subscription(models.Model):
    title=models.CharField(max_length=100)
    image=models.ImageField(upload_to='images/', blank=True, null=True)
    description=models.TextField(blank=True, null=True)
    name=models.CharField(max_length=100)
    email=models.EmailField(max_length=100)
    
    def __str__(self):
        return self.title
    
# class Footer(models.Model):
#     name = models.CharField(max_length=255)
#     value = models.CharField(max_length=255)
#     def __str__(self):
#         return self.name
    
# class Copyright(models.Model):
#     name = models.CharField(max_length=255)
#     value = models.CharField(max_length=255)
#     def __str__(self):
#         return self.name
    
# class MetaTags(models.Model):
#     name = models.CharField(max_length=255)
#     value = models.CharField(max_length=255)
#     def __str__(self):
#         return self.name