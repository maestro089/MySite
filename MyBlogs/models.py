from django.utils import timezone
import datetime
from django.db import models


class Blog(models.Model):
    DoesNotExist = None
    title = models.CharField(max_length=200)
    task = models.TextField()
    pub_date = models.DateTimeField(default=timezone.now(), verbose_name="Time published")
    cover = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return f'/MyBlogs/{self.id}'

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

