from django.shortcuts import render
from django.views.generic import View
# Create your views here.
from .models import About
def home(request):
    return render(request, "home.html")
from django.views.generic import (
    ListView,

)

from settings.models import General,HomePage,HomePageCards, USP, Testimonials, Bonus, Trainer,Subscription

def HomePageView(request):
    items=HomePage.objects.all()
    cards=HomePageCards.objects.all()
    usps=USP.objects.all()
    testimonials=Testimonials.objects.all()
    bonuses=Bonus.objects.all()
    trainers=Trainer.objects.all()
    subscriptions=Subscription.objects.all()
    return render(request, "home.html",{'items':items,'cards':cards,'usps':usps,'testimonials':testimonials,'bonuses':bonuses,'trainers':trainers,'subscriptions':subscriptions})
class AboutView(ListView):
    model = About
    template_name = "about.html"  # <app>/<model>_<viewtype>.html
    context_object_name = "about"
def error_404_handler(request, exception):
    return render(request, '404.html')