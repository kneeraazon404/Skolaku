from django.shortcuts import render
from django.views.generic import ListView
# Create your views here
from .models import General,HomePage
# class GeneralView(ListView):
#     model = General
#     template_name = "base.html"
#     context_object_name = "general"
    
# class HomepageView(ListView):
#     model = HomePage
#     template_name = "home.html"
#     context_object_name = "items"