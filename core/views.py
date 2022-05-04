from django.shortcuts import render
from django.views.generic import View
# Create your views here.
from .models import About
def home(request):
    return render(request, "home.html")
from django.views.generic import (
    ListView,

)


class AboutView(ListView):
    model = About
    template_name = "about.html"  # <app>/<model>_<viewtype>.html
    context_object_name = "about"
   