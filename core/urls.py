from django.urls import path
from .views import home,AboutView,HomePageView
urlpatterns = [
    path("",HomePageView, name="home"),
    path("about/", AboutView.as_view(), name="about"),

]
