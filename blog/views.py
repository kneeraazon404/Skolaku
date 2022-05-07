
from django.shortcuts import render, get_object_or_404
from django.core.mail import send_mail
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from .models import post, Course


class postListView(ListView):
    model = post
    template_name = "blog/blog.html"  # <app>/<model>_<viewtype>.html
    context_object_name = "posts"
    ordering = ["-date_posted"]
    paginate_by = 3

def detail_view(request, pk):
    blog = get_object_or_404(post, pk=pk)
    forms = post.objects.all()[:3]
    return render(request, 'blog/blog_detail.html', {'blog': blog, 'forms': forms})

class postCreateView(LoginRequiredMixin, CreateView):
    model = post
    fields = ["title", "content", "category", "excerpt", "image", "video", "date_posted","author"]

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class postUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = post
    fields = ["title", "content"]

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class postDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = post
    success_url = "/"

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

class CourseView(ListView):
    model = Course
    template_name = "blog/page-course.html"  # <app>/<model>_<viewtype>.html
    context_object_name = "courses"
    ordering = ["-date_created"]
    paginate_by = 6