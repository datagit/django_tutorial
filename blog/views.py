from django.shortcuts import render
from .models import Post
from django.http import Http404
# Create your views here.


def list(request):
    data = {'Posts': Post.objects.all().order_by('-date')}
    return render(request, 'blog/blog.html', data)


def detail(request, id):
    try:
        post = Post.objects.get(id=id)
    except Post.DoesNotExist:
        raise Http404("the post is not found")
    return render(request, 'blog/detail.html', {'post': post})
