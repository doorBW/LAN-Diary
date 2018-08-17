from django.forms import ModelForm
from .models import Category, Post

class MakeGroupFrom(ModelForm):
    class Meta:
        model = Category
        fields = ('C_name', 'C_detail', 'visible', 'anonymous')

class PostForm(ModelForm):
	class Meta:
		model = Post
		fields = ('title','photo','content','weather','emotion',)
