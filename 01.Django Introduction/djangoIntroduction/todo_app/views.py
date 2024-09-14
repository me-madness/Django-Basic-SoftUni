from django.http import HttpResponse
from django.shortcuts import render
# Create your views here.

def my_view(request):
    return HttpResponse("<h1>Main view</h1>") #MIME TYPE text/html


def add_view(request):
    return HttpResponse("<h1>Add view</h1>")


def delete_view(request):
    return HttpResponse("<h1>Delete view</h1>")