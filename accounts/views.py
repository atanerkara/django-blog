from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
from post.models import Post
from .models import Profile
from .forms import LoginForm, RegisterForm
from django.contrib.auth import authenticate, login, logout, get_user


# Create your views here.


def login_view(request):
    form = LoginForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        login(request, user)
        return redirect('home')
    return render(request, 'account/form.html', {'form': form, 'title': 'Sign in'})


def register_view(request):
    form = RegisterForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        password = form.cleaned_data.get('password')
        user.set_password(password)
        user.save()
        new_user = authenticate(username=user.username, password=password)
        login(request, new_user)
        return redirect('home')
    return render(request, 'account/form.html', {'form': form, 'title': 'Sign up'})


def logout_view(request):
    logout(request)
    return redirect('home')


def profile_view(request, username):
    user = User.objects.get(username=username)
    posts = Post.objects.filter()
    post_list = []
    for post in posts:
        if post.user == user:
            post_list.append(post)
    context = {
        'posts': post_list,
        'user': user,
    }
    return render(request, 'account/profile.html', context)
