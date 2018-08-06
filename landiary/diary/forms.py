from django.forms import ModelForm

from .models import Post 


class PostForm(ModelForm): #일단 긁어온 modelform, 후에 리팩토링하겠음.
    class Meta: 	
        model = Post
        fields = ['title',
                  'content',
                  'weather',
                  'emotion',
                  'category']


