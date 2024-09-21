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
        "ids": ["62348764", "fwnj825456", "865sdfg2654"]
    }
    return render(request, 'base.html', context)