from django.http import HttpResponse
from django.shortcuts import render
# Create your views here.

def my_view(request):
    return HttpResponse("<h1>Hello!</h1>") #MIME TYPE text/html