from datetime import datetime

from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    
    context = {
        "current_time": datetime.now()
    }
    return render(request, 'base.html', context)