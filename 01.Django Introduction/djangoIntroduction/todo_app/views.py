from django.http import HttpResponse
from django.shortcuts import render
from todo_app.models import Task
# Create your views here.

def index(request):
    tasks = Task.objects.all()
    
    result = '\n'.join([
        '<h1>TASKS</h1>',
        '<ul>',
        *[f"<li>{task.name}</li>" for task in tasks],
        '</ul>',
    ])
    
    print(result)
    
    return HttpResponse(result)