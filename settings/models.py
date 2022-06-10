
from django.db import models
from embed_video.fields import EmbedVideoField

# Create your models here.
class General(models.Model):
    name=models.CharField(max_length=100,default='General',editable=False)
    logo=models.ImageField(upload_to='images/', blank=True, null=True)
    favicon=models.ImageField(upload_to='images/', blank=True, null=True)
    whatsapp_no=models.CharField(max_length=20, blank=True, null=True)
    scripts_in_header = models.CharField(max_length=5000,blank=True)
    scripts_in_body = models.CharField(max_length=5000,blank=True)
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "General"
        verbose_name_plural = "General"

class MenuLink(models.Model):
    url = models.URLField(max_length=200)
    link_text = models.CharField(max_length=30)

    def __str__(self):
        return self.link_text

class HomePageCards(models.Model):
    card_image=models.ImageField(upload_to='images/', blank=True, null=True)
    card_title=models.CharField(max_length=100)
    card_desc=models.TextField(blank=True, null=True)
    
    def __str__(self):
        return self.card_title
    
    class Meta:
        verbose_name = "Home Page Course List"
        verbose_name_plural = "Home Page Course List"

class HomePage(models.Model):
    title=models.CharField(max_length=100)
    usp_title=models.CharField(max_length=100)
    bonus_title=models.CharField(max_length=100)
    testmonial_title=models.CharField(max_length=100)
    trainer_title=models.CharField(max_length=100)
    excerpt=models.TextField(blank=True, null=True)
    hero_img=models.ImageField(upload_to='images/', blank=True, null=True)
    featured_img=models.ImageField(upload_to='images/', blank=True, null=True)
    home_product_title=models.CharField(max_length=100,verbose_name='Home Product Title')

    def __str__(self):
        return self.title
    
class USP(models.Model):
    card_title=models.CharField(max_length=100, blank=True, null=True)
    card_img=models.ImageField(upload_to='images/', blank=True, null=True)
    card_desc=models.TextField(blank=True, null=True)
    
    def __str__(self):
        return self.card_title
    

class Testimonials(models.Model):
    image=models.ImageField(upload_to='images/', blank=True, null=True)
    video = EmbedVideoField(max_length=140, default="", blank=True)
    description=models.TextField(blank=True, null=True)
    
    def __str__(self):
        return "Testimonial"
    
    class Meta:
        verbose_name = "Testimonial"
        verbose_name_plural = "Testimonials"
    
class Bonus(models.Model):
    card_title=models.CharField(max_length=100)
    image=models.ImageField(upload_to='images/', blank=True, null=True)
    
    def __str__(self):
        return self.card_title

    class Meta:
        verbose_name = "Bonus"
        verbose_name_plural = "Bonuses"
    
class Trainer(models.Model):
    image=models.ImageField(upload_to='images/', blank=True, null=True)
    name=models.CharField(max_length=100)
    occupation=models.CharField(max_length=100)
    linkedin=models.URLField(max_length=100, blank=True, null=True)
    
    def __str__(self):
        return self.name
class Subscription(models.Model):
    title=models.CharField(max_length=100)
    image=models.ImageField(upload_to='images/', blank=True, null=True)
    description=models.TextField(blank=True, null=True)
    # name=models.CharField(max_length=100)
    # email=models.EmailField(max_length=100)
    
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