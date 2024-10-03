from django.urls import path, include # type: ignore

from petstagram.accounts import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login', views.login, name='login'),
    path('profile/<int:pk>/', include([
        path('', views.profile_details, name='profile-details'),
        path('edit/', views.edit_profile, name='profile-edit'),
        path('delete', views.delete_profile, name='profile-delete'),
    ]))
]