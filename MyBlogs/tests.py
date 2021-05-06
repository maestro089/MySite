import datetime

from django.template import context
from django.test import TestCase
from django.utils import timezone
from django.urls import reverse

from .models import Blog
from .views import create

def create_blog(title, days):
    time = timezone.now() + datetime.timedelta(days=days)
    return Blog.objects.create(title=title, pub_date=time)


class BlogModelTests(TestCase):

    def test_was_published_with_future_blog(self):
        time = timezone.now() + datetime.timedelta(days=30)
        future_blog = Blog(pub_date=time)
        self.assertIs(future_blog.was_published_recently(), True)


    def test_was_published_with_old_blog(self):
        time = timezone.now() + datetime.timedelta(days=1, seconds=1)
        future_blog = Blog(pub_date=time)
        self.assertIs(future_blog.was_published_recently(), True)


    def test_was_published_with_recent_blog(self):
        time = timezone.now() - datetime.timedelta(hours=23, minutes=59, seconds=59)
        future_blog = Blog(pub_date=time)
        self.assertIs(future_blog.was_published_recently(), True)


class BlogIndexViewTests(TestCase):
    def test_no_blogs(self):
        response = self.client.get(reverse('MyBlogs:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No blogs are available.")
        self.assertQuerysetEqual(response.context['latest_blog_list'], [])

    def test_past_blog(self):
        create_blog(title="Past blog", days=-30)
        response = self.client.get(reverse('MyBlogs:index'))
        self.assertQuerysetEqual(
            response.context['latest_blog_list'],
            ['<Blog: Past blog>']
        )

    def test_future_question(self):
        create_blog(title="Future blog.", days=30)
        response = self.client.get(reverse('MyBlogs:index'))
        self.assertContains(response, "No blogs are available.")
        self.assertQuerysetEqual(response.context['latest_blog_list'], [])
