from django.shortcuts import render
from .models import News_post

# Create your views here.
def home(request):
    news = News_post.objects.all()
    return render(request, 'news1/news1.html', {'news': news})

def create_news(request):
    return render(request, 'news1/add_new_post.html')