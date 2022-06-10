from django.shortcuts import render
from django.views.generic import View
# Create your views here.
from .models import About
def home(request):
    return render(request, "home.html")
from django.views.generic import (
    ListView,

)
import random
from blog.models import post

from settings.models import General,HomePage,HomePageCards, USP, Testimonials, Bonus, Trainer,Subscription

def HomePageView(request):
    general = General.objects.latest('name')
    items=HomePage.objects.all()
    cards=HomePageCards.objects.order_by('card_title')
    usps=USP.objects.all()
    testimonials=Testimonials.objects.all()
    bonuses=Bonus.objects.all()
    trainers=Trainer.objects.all()
    subscriptions=Subscription.objects.all()
    return render(request, "home.html",{'general':general,'items':items,'cards':cards,'usps':usps,'testimonials':testimonials,'bonuses':bonuses,'trainers':trainers,'subscriptions':subscriptions})
class AboutView(ListView):
    model = About
    template_name = "about.html"  # <app>/<model>_<viewtype>.html
    context_object_name = "about"

def error_404_handler(request, exception):
    post_list = post.objects.all()
    post_list_random = random.choices(post_list, k=3)

    return render(request, '404.html',{'post_list_random' : post_list_random,})