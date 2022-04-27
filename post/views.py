from django.shortcuts import render, get_object_or_404, HttpResponse, HttpResponseRedirect, redirect, Http404
from .models import Post, Comment
from .forms import PostForm, CommentForm
from django.contrib import messages
from django.core.paginator import Paginator
from django.shortcuts import render
from django.db.models import Q
# Create your views here.


def post_index(request):
    post_list = Post.objects.all()
    query = request.GET.get('q')
    if query:
        post_list = post_list.filter(
            Q(title__icontains= query) |
            Q(content__icontains=query)
        ).distinct()
    paginator = Paginator(post_list, 5)  # Show 25 contacts per page.

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'post/index.html', {'posts': page_obj})


def post_create(request):
    if not request.user.is_authenticated:
        return Http404()

    form = PostForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        post = form.save(commit=False)
        post.user = request.user
        post.save()
        messages.success(request, 'Post created successfully.')
        return HttpResponseRedirect(post.get_absolute_url())

    context = {
        'form': form,
    }
    return render(request, 'post/form.html', context)


def post_delete(request, slug):
    if not request.user.is_authenticated():
        return Http404()
    post = get_object_or_404(Post, slug=slug)
    if post.user != request.user and not request.user.is_staff:
        return Http404()
    post.delete()
    messages.success(request, 'Post deleted successfully.')
    return redirect('post:index')


def post_update(request, slug):
    if not request.user.is_authenticated:
        return Http404()
    post = get_object_or_404(Post, slug=slug)
    form = PostForm(request.POST or None, request.FILES or None, instance=post)
    if post.user != request.user and not request.user.is_staff:
        return Http404()
    if form.is_valid():
        form.save()
        messages.success(request, 'Post updated successfully.')
        return HttpResponseRedirect(post.get_absolute_url())
    context = {
        'form': form,
    }
    return render(request, 'post/form.html', context)


def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)

    form = CommentForm(request.POST or None)
    if form.is_valid():
        if not request.user.is_authenticated:
            messages.warning(request, 'Please log in to post comment')
            return HttpResponseRedirect(post.get_absolute_url())
        comment = form.save(commit=False)
        comment.user = request.user
        comment.post = post
        comment.save()
        return HttpResponseRedirect(post.get_absolute_url())

    if request.GET.get('commentDelete'):
        comment = Comment.objects.get(pk=request.GET.get('commentDelete'))
        if comment.user == request.user or request.user.is_staff:
            comment.delete()
            messages.success(request, 'Comment deleted successfully')

    context = {
        'post': post,
        'form': form,
    }
    return render(request, 'post/detail.html', context)


def post_disable(request, slug):
    if not request.user.is_authenticated:
        return Http404()
    post = get_object_or_404(Post, slug=slug)
    if request.user == post.user or request.user.is_staff:
        if post.is_disabled:
            post.is_disabled = False
            messages.success(request, 'Post enabled for comments successfully')
        else:
            post.is_disabled = True
            messages.success(request, 'Post disabled for comments')
    else:
        return Http404()
    post.save()
    return HttpResponseRedirect(post.get_absolute_url())