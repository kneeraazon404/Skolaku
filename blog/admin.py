from django.contrib import admin

# Register your models here.
from .models import  post, Category,ParentCategory, Course

class PostAdmin(admin.ModelAdmin):
    exclude = ('author',)
    list_display = ('title','author',)

    def has_change_permission(self, request, obj=None):
        has_class_permission = super(PostAdmin, self).has_change_permission(request, obj)
        if not has_class_permission:
            return False
        if obj is not None and not request.user.is_superuser and request.user.id != obj.author.id:
            return False
        return True

    def queryset(self, request):
        if request.user.is_superuser:
            return post.objects.all()
        return post.objects.filter(author=request.user)
    
    # def has_delete_permission(self, request, obj=None):
    #     return False

    def save_model(self, request, obj, form, change):
        if not change:
            obj.author = request.user
        obj.save()
    

admin.site.register(post,PostAdmin)
admin.site.register(Category)
# admin.site.register(ParentCategory)
admin.site.register(Course)
