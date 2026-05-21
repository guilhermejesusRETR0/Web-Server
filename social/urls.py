from django.urls import path

from . import views

app_name = 'social'

urlpatterns = [
    path('', views.home, name='home'),
    path('feed/', views.feed, name='feed'),
    path('utilizador/<str:username>/', views.user_posts, name='user_posts'),
]
