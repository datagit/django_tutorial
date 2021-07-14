from django.test import TestCase
from .models import Post
# Create your tests here.


class BlogTests(TestCase):
    def setUp(self):
        # 1. first call when class run
        Post.objects.create(
            title='myTitle',
            body='myBody'
        )

    def test_def_to_string(self):
        post = Post(title='my entry title')
        # verify def __str__
        self.assertEqual(str(post), post.title)

    def test_blog_list_view(self):
        response = self.client.get('/blog/')
        # verify status_code
        self.assertEqual(response.status_code, 200)
        # verify title
        self.assertContains(response, 'myTitle')
        # verify template used
        self.assertTemplateUsed(response, 'blog/blog.html')

    def test_blog_detail_view(self):
        response = self.client.get('/blog/1/')
        # verify status_code
        self.assertEqual(response.status_code, 200)
        # verify title
        self.assertContains(response, 'myTitle')
        # verify template used
        self.assertTemplateUsed(response, 'blog/detail.html')
