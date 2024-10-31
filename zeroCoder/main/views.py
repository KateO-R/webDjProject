from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    return HttpResponse("<h1>This is my first Django Project!</h1>")
def new(request):
    return HttpResponse("<h1>This is second page of the Django Project!</h1>")