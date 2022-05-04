
  
from django.urls import path
from .views import (
    postListView,
    detail_view,
    postCreateView,
    postUpdateView,
    postDeleteView,
    CourseView
)
from . import views

urlpatterns = [
    path("", postListView.as_view(), name="blog-home"),
    path("page-course/", CourseView.as_view(), name="page-course"),

    path("post/<int:pk>/", detail_view, name="post-detail"),
    path("post/new/", postCreateView.as_view(), name="post-create"),
    path("post/<int:pk>/update/", postUpdateView.as_view(), name="post-update"),
    path("post/<int:pk>/delete/", postDeleteView.as_view(), name="post-delete"),
]


