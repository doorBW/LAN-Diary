import datetime
from django.contrib.postgres.fields import ArrayField
from django.db import models
from django.utils import timezone


class Category(models.Model):
    C_name = models.CharField(max_length=100)
    C_detail = models.CharField(max_length=1000)
    visible = models.IntegerField(default=1)
    anonymous = models.IntegerField(default=0)
    link = models.CharField(max_length=1000, default="http://localhost:8000/main/groupdiary/all")
    def __str__(self):
        return "%s" % (self.C_name)

from login.models import User

class Post(models.Model):
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='../media/',blank=True, null=True)
    content = models.CharField(max_length=4000)
    published = models.DateTimeField(auto_now=True)
    weather = models.CharField(max_length=15)
    emotion = models.CharField(max_length=15)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, blank=True, null=True)
    timeout = models.IntegerField(default=0)

    def __str__(self):
        return "%s - %s" % (self.username, self.title)

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    content = models.CharField(max_length=200)
    author = models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
    created = models.DateTimeField(auto_now=True)
    def __str__(self):
        return "%s 의 댓글" % (self.post)

class PickPost(models.Model):
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    pick_posts = models.ManyToManyField(Post, blank=True)
    def __str__(self):
        return "%s의 뜯어온일기" % (self.username)
