from django.urls import path
from . import views
urlpatterns = [
    path('', views.blog, name='blog'),
    path("<int:blog_id>/", views.blog_detail, name="blog_detail"),
    path("page_course/", views.page_course, name="page_course"),

]
