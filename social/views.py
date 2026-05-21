from django.shortcuts import render


def home(request):
    return render(request, 'social/home.html')


def feed(request):
    return render(request, 'social/feed.html')


def user_posts(request, username):
    context = {'username': username}
    return render(request, 'social/user_posts.html', context)
