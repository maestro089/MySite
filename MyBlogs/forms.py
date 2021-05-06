from django.forms import ModelForm, TextInput, Textarea, DateTimeField
from .models import Blog


class CreateForm(ModelForm):
   class Meta:
       model = Blog
       fields = ['title', 'task', 'pub_date', 'cover']

       widgets = {
           "title": TextInput(attrs={
               'class': 'form-control',
               'placeholder': 'Название блога'
           }),
           'task': Textarea(attrs={
               'class': 'form-control',
               'placeholder': 'Текст блог'
           }),

    }