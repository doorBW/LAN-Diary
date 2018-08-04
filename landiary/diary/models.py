import datetime

from django.db import models
from django.utils import timezone


class Post(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    content = models.TextField()
    published_date = models.DateTimeField(default=timezone.now)
    weather = models.CharField(max_length=15)
    emotion = models.CharField(max_length=15)
    category = models.CharField(max_length=15)
    anonymous = models.IntegerField(default=0)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return "%s - %s" % (self.user, self.title)

