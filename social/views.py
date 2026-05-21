from django.db.models import F
from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.http import require_POST

from .models import Comment, Post, Profile


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


@require_POST
def like_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    Post.objects.filter(id=post.id).update(likes=F('likes') + 1)
    return redirect(request.POST.get('next', 'social:feed'))


@require_POST
def add_comment(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    username = request.POST.get('username', '').strip().lower()
    content = request.POST.get('content', '').strip()

    if username and content:
        profile, _ = Profile.objects.get_or_create(
            username=username,
            defaults={'full_name': username.title(), 'bio': 'Fã de JoJo em Morioh.'},
        )
        Comment.objects.create(post=post, author=profile, content=content)

    return redirect(request.POST.get('next', 'social:feed'))
