from django.core.exceptions import PermissionDenied
from django.shortcuts import render

# Create your views here.
from django.http import Http404
from django.http import HttpResponse
from django.shortcuts import render

from tags.models import Tag
from .models import Blog
from .forms import BlogForm

def detail(request):

    if request.method == "POST":
        form = BlogForm(request.POST)
        if form.is_valid():
            blog = form.save(commit=False)
            blog.owner = request.user
            blog.save()
            form.save_m2m()

    elif request.method == "GET":
        form = BlogForm()

    return render(request, "blog/detail.html", {"blogs": Blog.objects.filter(owner=request.user.id),
                                             "tags":Tag.objects.all(),
                                             "form": form})


def index(request, blog_id):
    try:
        blog = Blog.objects.get(id=blog_id)
        if request.user.id != blog.owner.id:
            raise PermissionDenied
        return render(request, "blog/index.html", {"blog": blog})
    except Blog.DoesNotExist:
        raise Http404("We don't have any.")