from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("<h1>This is the first page of MyApp!</h1>")
def data(request):
    return HttpResponse("<h1>This is the data page of MyApp!</h1>")

def test(request):
    return HttpResponse("<h1>This is the test page of MyApp!</h1>")