from multiprocessing import context
from django.shortcuts import render, get_object_or_404
from django.core.mail import send_mail
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.views import View
from django.core.paginator import Paginator

from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from requests import request
from .models import post, Course


class postListView(ListView):
    model = post
    template_name = "blog/blog.html"  # <app>/<model>_<viewtype>.html
    context_object_name = "posts"
    ordering = ["-date_posted"]
    paginate_by = 1


def detail_view(request, slug):
    blog = get_object_or_404(post, slug=slug)
    forms = post.objects.all()[:3]
    return render(request, "blog/blog_detail.html", {"blog": blog, "forms": forms})


class postCreateView(LoginRequiredMixin, CreateView):
    model = post
    fields = [
        "title",
        "content",
        "category",
        "excerpt",
        "image",
        "video",
        "date_posted",
        # "author",
    ]

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

from settings.models import HomePageCards, USP, Testimonials, Bonus, Trainer,General
from django.core.paginator import Paginator
class CourseView(ListView):
    model = Course
    template_name = "blog/page-course.html"  # <app>/<model>_<viewtype>.html
    paginate_by = 1
    
    def get(self, request, *args, **kwargs):

        course = Course.objects.all().order_by('-date_created')
        paginator = Paginator(course, 10)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)

        general = General.objects.latest('name')
        cards=HomePageCards.objects.order_by('card_title')
        usps=USP.objects.all()
        testimonials=Testimonials.objects.all()
        bonuses=Bonus.objects.all()
        trainers=Trainer.objects.all()
        context = {
            'general':general,
            'course':course,
            'cards':cards,
            'usps':usps,
            'testimonials':testimonials,
            'bonuses':bonuses,
            'trainers':trainers,
            'page_obj': page_obj
        }

        return render(request, self.template_name ,context)

from .models import Category,post

def blogCategory(request):
    category = Category.objects.all().order_by('name')
    post_list = post.objects.all()
    paginator = Paginator(category, 5) 
    paginate_by = 1
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'category':category,
        'post_list':post_list,
        'page_obj':page_obj,
    }
    print('Hey')
    return render(request,'blog/blog-category.html',context= context)
from django.db.models import Q
def search(request):
    post_list = post.objects.all()

    keyword = request.GET['keyword']
    if 'keyword' in request.GET:
        keyword = request.GET['keyword']
        if keyword:
            post_list = post_list.filter(Q(content__icontains = keyword) | Q(title__icontains = keyword) | Q(excerpt__icontains = keyword))

    context = {
        'post_list':post_list,
        'keyword':keyword,
    }
    
    return render(request,'blog/blog-search-result.html',context)
