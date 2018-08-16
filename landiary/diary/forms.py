from django.forms import ModelForm

from .models import Post

# class PostForm(ModelForm):
# 	class Meta:
# 		model = Post

class PostForm(ModelForm):
	class Meta:
		model = Post
		fields = ('title','photo','content','weather','emotion',)


'''

	username = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    photo = models.ImageField()
    content = models.CharField(max_length=4000)
    published = models.DateTimeField(auto_now=True)
    weather = models.CharField(max_length=15)
    emotion = models.CharField(max_length=15)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, blank=True, null=True)
    timeout = models.IntegerField(default=0)
'''