from django.forms import ModelForm
from .models import Category

class MakeGroupFrom(ModelForm):
    class Meta:
        model = Category
        fields = ('C_name', 'C_detail', 'visible', 'anonymous')
