from django.urls import path
from todo_app.views import my_view, add_view, delete_view

urlpatterns = [
    path('', my_view),
    path('add/', add_view),
    path('delete/', delete_view),
]


