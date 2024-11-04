from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, 'MyApp/index.html')
def news(request):
    return render(request, 'MyApp/news.html')
def fun(request):
    return render(request, 'MyApp/fun.html')
def table(request):
    return render(request, 'MyApp/table.html')
