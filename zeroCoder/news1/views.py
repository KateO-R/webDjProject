from django.shortcuts import render, redirect
from .models import News_post
from .forms import News_postForm

# Create your views here.
def home(request):
    news = News_post.objects.all()
    return render(request, 'news1/news1.html', {'news': news})

def create_news(request):
    error = ''
    if request.method == 'POST':
        form = News_postForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('news1_home')
        else:
            error = 'Incorrectly filled data'
    form = News_postForm()
    return render(request, 'news1/add_new_post.html', {'form': form, 'errors': error})