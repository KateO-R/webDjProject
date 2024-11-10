from .models import News_post
from django.forms import ModelForm, TextInput, Textarea, DateTimeInput

class News_postForm(ModelForm):
    class Meta:
        model = News_post
        fields = ['title', 'short_description', 'text', 'pub_date', 'author']
        widgets = {
            'title': TextInput(attrs={'class': 'form-control', 'placeholder': 'Post title'}),
            'author': TextInput(attrs={'class': 'form-control', 'placeholder': 'Author name'}),
            'short_description': TextInput(attrs={'class': 'form-control', 'placeholder': 'Short description'}),
            'text': Textarea(attrs={'class': 'form-control', 'placeholder': 'Main text'}),
            'pub_date': DateTimeInput(attrs={'class': 'form-control', 'placeholder': 'Post date'})
        }