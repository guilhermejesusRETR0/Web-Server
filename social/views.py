from django.shortcuts import get_object_or_404, render

from .models import Post, Profile


def home(request):
    total_profiles = Profile.objects.count()
    total_posts = Post.objects.count()
    recent_posts = Post.objects.select_related('author')[:5]
    context = {
        'total_profiles': total_profiles,
        'total_posts': total_posts,
        'recent_posts': recent_posts,
    }
    return render(request, 'social/home.html', context)


def feed(request):
    posts = Post.objects.select_related('author').prefetch_related('comments__author')
    context = {'posts': posts}
    return render(request, 'social/feed.html', context)


def user_posts(request, username):
    profile = get_object_or_404(Profile, username=username)
    posts = profile.posts.prefetch_related('comments__author')
    context = {'profile': profile, 'posts': posts}
    return render(request, 'social/user_posts.html', context)
