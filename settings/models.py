from multiprocessing.sharedctypes import Value
from unicodedata import name
from django.db import models

# Create your models here.
class General(models.Model):
    name = models.CharField(max_length=255)
    value = models.CharField(max_length=255)
    def __str__(self):
        return self.name
    
class HomePage(models.Model):
    name = models.CharField(max_length=255)
    value = models.CharField(max_length=255)
    def __str__(self):
        return self.name
    
    
class USP(models.Model):
    name = models.CharField(max_length=255)
    value = models.CharField(max_length=255)
    def __str__(self):
        return self.name
    

class Testimonials(models.Model):
    name = models.CharField(max_length=255)
    value = models.CharField(max_length=255)
    def __str__(self):
        return self.name
    
class Bonus(models.Model):
    name = models.CharField(max_length=255)
    value = models.CharField(max_length=255)
    def __str__(self):
        return self.name
    
class Trainer(models.Model):
    name = models.CharField(max_length=255)
    Value = models.CharField(max_length=255)
    def __str__(self):
        return self.Value

class Subscription(models.Model):
    name = models.CharField(max_length=255)
    Value = models.CharField(max_length=255)
    def __str__(self):
        return self.Value
    
class Footer(models.Model):
    name = models.CharField(max_length=255)
    value = models.CharField(max_length=255)
    def __str__(self):
        return self.name
    
class Copyright(models.Model):
    name = models.CharField(max_length=255)
    value = models.CharField(max_length=255)
    def __str__(self):
        return self.name
    
class MetaTags(models.Model):
    name = models.CharField(max_length=255)
    value = models.CharField(max_length=255)
    def __str__(self):
        return self.name