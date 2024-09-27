from datetime import datetime

from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    
    context = {
        "current_time": datetime.now(),
        "person": {
            "age": 20,
            "height": 190,
        },
        "ids": ["658921deer", "1232544dss", "4785swrs55"],
        "some_text": "Hello",
        "users": [
            "Pesho",
            "Ivan",
            "Dragan",
            "Kukumicin",
            "Milen"
        ]
    }    
    
    
    return render(request, 'base.html', context)


def dashboard(request):
    context = {
        "posts": [
            {
                "title": "How to create django project?",
                "author": "Rangel Petrov",
                "content": "I really don't know how to create a project",
                "created_at": datetime.now(),
            },
            {
                "title": "How to create Angular project?",
                "author": "Boris Petrov",
                "content": "I really don't know how to create a project",
                "created_at": datetime.now(),
            },
            {
                "title": "How to create React project?",
                "author": "Samuil Petrov",
                "content": "I really don't know how to create a project",
                "created_at": datetime.now(),
            }
        ]
    }
    
    return render(request, 'posts/dashboard.html', context)