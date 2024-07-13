from django.shortcuts import render, get_object_or_404

from blog.models import Category
from .constants import MAINPAGE_MAX_POSTS
from .helper import get_queryset


def index(request):
    post_list = get_queryset()[:MAINPAGE_MAX_POSTS]
    context = {
        'post_list': post_list,
    }
    return render(request, 'blog/index.html', context)


def post_detail(request, post_id):
    post = get_object_or_404(get_queryset(), id=post_id)
    context = {
        'post': post,
    }
    return render(request, 'blog/detail.html', context)


def category_posts(request, category_slug):
    category = get_object_or_404(
        Category, is_published=True, slug=category_slug)
    post_list = get_queryset().filter(category=category)
    context = {
        'post_list': post_list,
        'category': category,
    }
    return render(request, 'blog/category.html', context)
