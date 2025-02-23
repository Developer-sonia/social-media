# posts/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.create_post, name='create_post'),
    path('', views.home, name='home'),
    path('profile/', views.profile, name='profile'),
]
