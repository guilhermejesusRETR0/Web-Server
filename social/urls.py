from django.urls import path

from . import views

app_name = 'social'

urlpatterns = [
    path('', views.home, name='home'),
    path('feed/', views.feed, name='feed'),
    path('utilizador/<str:username>/', views.user_posts, name='user_posts'),
    path('post/<int:post_id>/like/', views.like_post, name='like_post'),
    path('post/<int:post_id>/comment/', views.add_comment, name='add_comment'),
]
