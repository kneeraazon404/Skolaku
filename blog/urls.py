from django.urls import path
from .views import (
    postListView,
    CourseView,
)
from . import views

urlpatterns = [
    path("", postListView.as_view(), name="blog-home"),
    path("page-course/", CourseView.as_view(), name="page-course"),
]
