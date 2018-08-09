from diary.models import Category
from django.db import models


# Create your models here.
class User(models.Model):
    nick_name = models.CharField(max_length=40)
    email = models.CharField(max_length=100)
    categories = models.ManyToManyField(Category, blank=True)
    def __str__(self):
        return "%s" % (self.nick_name)



