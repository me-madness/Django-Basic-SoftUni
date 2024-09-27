from django.urls import path
from posts.views import dashboard, index

urlpatterns = [
    path('', index, name='index'),
    path('dashboard/', dashboard, name='dashboard'),
]
