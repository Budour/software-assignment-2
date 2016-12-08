from django.http import Http404
from django.shortcuts import render
from .models import Blog

def index(request):
    return render(request, "blog/detail.html", {"blogs": Blog.objects.all()})


def detail(request, blog_id):
    try:
        blog = Blog.objects.get(id=blog_id)
        return render(request, "blog/index.html", {"blog": blog})
    except Blog.DoesNotExist:
        raise Http404("We don't have any.")

