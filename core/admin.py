from django.contrib import admin
from .models import About,profile
# Register your models here.

class AboutAdmin(admin.ModelAdmin):
    model: About

    def has_delete_permission(self, request, obj=None):
        return False

    def has_add_permission(self, request):
        return False if self.model.objects.count() > 0 else super().has_add_permission(request)


admin.site.register(About,AboutAdmin)
admin.site.register(profile)