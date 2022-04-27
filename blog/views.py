from django.shortcuts import render

# Create your views here.
def blog(request):
    return render(request, 'blog/blog.html')

def blog_detail(request, blog_id):
    return render(request, 'blog/blog_detail.html')

def page_course(request):
    return render(request, 'blog/page-course.html')

