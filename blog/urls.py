from django.urls import path
from .views import (
    postListView,
)
from . import views

urlpatterns = [
    path("", postListView.as_view(), name="blog-home"),
]
