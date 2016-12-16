from django.core.exceptions import PermissionDenied
from django.shortcuts import render

# Create your views here.
from django.http import Http404
from django.shortcuts import render
from tags.models import Tag
from .models import Blog

def detail(request):

    if request.method == "POST":
        blog = Blog.objects.create(name=request.POST.get("blog_name"),
                            surname=request.POST.get("surname_name"),
                            owner=request.user)

        blog.tags.add(*request.POST.getlist("tag_names"))


    return render(request, "blog/detail.html", {"blogs": Blog.objects.filter(owner=request.user.id),
                                             "tags":Tag.objects.all()})


def index(request, blog_id):
    try:
        blog = Blog.objects.get(id=blog_id)
        if request.user.id != blog.owner.id:
            raise PermissionDenied
        return render(request, "blog/index.html", {"blog": blog})
    except Blog.DoesNotExist:
        raise Http404("We don't have any.")