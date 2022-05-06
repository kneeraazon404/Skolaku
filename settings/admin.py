from re import A
from django.contrib import admin
from .models import General, HomePage, USP, Testimonials, Bonus, Trainer, Subscription,HomePageCards
# Register your models here.

admin.site.register(General)
admin.site.register(HomePage)
admin.site.register(USP)
admin.site.register(Testimonials)
admin.site.register(Bonus)
admin.site.register(Trainer)
admin.site.register(Subscription)
admin.site.register(HomePageCards)
# admin.site.register(Footer)
# admin.site.register(Copyright)
# admin.site.register(MetaTags)