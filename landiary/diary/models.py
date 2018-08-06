import datetime
from django.contrib.postgres.fields import ArrayField
from django.db import models
from django.utils import timezone


class Category(models.Model):
    C_name = models.CharField(max_length=100)
    C_detail = models.CharField(max_length=1000)
    visible = models.IntegerField(default=1)
    anonymous = models.IntegerField(default=0)
    link = models.CharField(max_length=1000,blank=True,null=True)
    def __str__(self):
        return "%s" % (self.C_name)

# class Post(models.Model):
#     title = models.CharField(max_length=100)
#     content = models.CharField(max_length=4000)
#     author = models.CharField(max_length=40)
#     emo = models.CharField(max_length=40)
#     weather = models.CharField(max_length=40)
#     timeout = models.IntegerField(default=0)
#     likes = models.IntegerField(default=0)
#     comments = models.ForeignKey(Comment)
#     created = models.DateTimeField(auto_now=True)
    

class Post(models.Model):
    user = models.ForeignKey('login.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    content = models.CharField(max_length=4000)
    published = models.DateTimeField(auto_now=True)
    weather = models.CharField(max_length=15)
    emotion = models.CharField(max_length=15)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, blank=True, null=True)
    timeout = models.IntegerField(default=0)
    comments = ArrayField(
        models.CharField(max_length=100),
        null=True,
        blank=True
    )
    # def publish(self):
    #     self.published_date = timezone.now()
    #     self.save()

    def __str__(self):
        return "%s - %s" % (self.user, self.title)

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    content = models.CharField(max_length=200)
    author = models.ForeignKey('login.User',on_delete=models.SET_NULL,null=True)
    created = models.DateTimeField(auto_now=True)
    def __str__(self):
        return "%s 의 댓글" % (self.post)