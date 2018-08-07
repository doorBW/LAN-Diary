from django.contrib.postgres.fields import ArrayField
from diary.models import Category
from django.db import models


# Create your models here.
class User(models.Model):
    nick_name = models.CharField(max_length=40)
    email = models.CharField(max_length=100)
    posts = ArrayField(
        models.CharField(max_length=100,blank=True),
        blank=True,
        null=True
    )
    categories = models.ManyToManyField(Category, blank=True, null=True)
    def __str__(self):
        return "%s" % (self.nick_name)



