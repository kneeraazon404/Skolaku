from django.urls import path
from .views import home,AboutView
urlpatterns = [
    path("",home, name="home"),
    path("about/", AboutView.as_view(), name="about"),

]
