from django.contrib import admin

# Register your models here.
from .models import  post, Category,ParentCategory, Course


admin.site.register(post)
admin.site.register(Category)
admin.site.register(ParentCategory)
admin.site.register(Course)
