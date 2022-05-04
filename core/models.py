from tabnanny import verbose

from ckeditor.fields import RichTextField
from django.db import models

        
from django.contrib.auth.models import User
from django.db import models
from PIL import Image

# Create your models here.
class About(models.Model):
    title = models.CharField(max_length=100)
    description = RichTextField()
    
    class Meta:
        verbose_name = "About"
        verbose_name_plural = "About"
    
    def __str__(self):
        return self.title
    

class profile(models.Model):
    first_name = models.CharField(max_length=100, verbose_name="First Name")
    last_name = models.CharField(max_length=100, verbose_name="Last Name")
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name="User")
    email=models.EmailField(max_length=100, verbose_name="Email")
    biographical_info = models.TextField(max_length=500, blank=True, verbose_name="Biographical Info")
    image = models.ImageField(default="default.jpg", upload_to="profile_pics", verbose_name="Profile Picture")


    def __str__(self):
        return f"{self.user.username} Profile"
    def set_email(self):
        return self.user.email
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)
