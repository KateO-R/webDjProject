from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, 'MyApp/index.html')
def news(request):
    return render(request, 'MyApp/news.html')

def test(request):
    return HttpResponse("<h1>This is the test page of MyApp!</h1>")