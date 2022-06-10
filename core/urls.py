from django.urls import path
from .views import home,AboutView,HomePageView
from blog.views import CourseView,blogCategory,search
urlpatterns = [
    path("",HomePageView, name="home"),
    path("about/", AboutView.as_view(), name="about"),
    path("page-course/", CourseView.as_view(), name="page-course"),
    path("blog-category/", blogCategory, name="page-course"),
    path("search", search, name="search"),
]
