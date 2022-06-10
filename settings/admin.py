from re import A
from django.contrib import admin
from .models import General,MenuLink , HomePage, USP, Testimonials, Bonus, Trainer, Subscription,HomePageCards
# Register your models here.

class TestimonialsAdmin(admin.ModelAdmin):
    list_display = ("description", )

class SubscriptionAdmin(admin.ModelAdmin):
    model: Subscription

    def has_delete_permission(self, request, obj=None):
        return False

    def has_add_permission(self, request):
        return False if self.model.objects.count() > 0 else super().has_add_permission(request)

class GeneralAdmin(admin.ModelAdmin):
    model: General

    def has_delete_permission(self, request, obj=None):
        return False

    def has_add_permission(self, request):
        return False if self.model.objects.count() > 0 else super().has_add_permission(request)

admin.site.register(General,GeneralAdmin)
admin.site.register(MenuLink)
admin.site.register(HomePage)
admin.site.register(USP)
admin.site.register(Testimonials,TestimonialsAdmin)
admin.site.register(Bonus)
admin.site.register(Trainer)
admin.site.register(Subscription, SubscriptionAdmin)
admin.site.register(HomePageCards)
# admin.site.register(Footer)
# admin.site.register(Copyright)
# admin.site.register(MetaTags)