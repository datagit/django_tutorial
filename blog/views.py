from django.shortcuts import render
from .models import Post
from django.http import Http404
# import the logging library
import logging

# Create your views here.

# Get an instance of a logger
logger = logging.getLogger('mysite.logging.console')

def list(request):
    data = {'Posts': Post.objects.all().order_by('-date')}
    logger.info("Init log from view")
    logger.warning("Init warning from view")
    logger.error("Test error")
    print('ABC')
    return render(request, 'blog/blog.html', data)


def detail(request, id):
    try:
        post = Post.objects.get(id=id)
    except Post.DoesNotExist:
        raise Http404("the post is not found")
    return render(request, 'blog/detail.html', {'post': post})
