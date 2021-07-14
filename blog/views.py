from django.shortcuts import render
from .models import Post
# Create your views here.


def list(request):
    data = {'Posts': Post.objects.all().order_by('-date')}
    return render(request, 'blog/blog.html', data)


def detail(request, id):
    post = Post.objects.get(id=id)
    return render(request, 'blog/detail.html', {'post': post})
