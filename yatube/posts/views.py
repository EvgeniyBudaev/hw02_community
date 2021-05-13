from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
import datetime as dt

from .models import Post, Group


def index(request):
    post_list = Post.objects.all().order_by('-pub_date')
    paginator = Paginator(post_list, 10)
    page_number = request.GET.get('page')
    page = paginator.get_page(page_number)
    current_year = dt.datetime.now().year
    return render(request, "index.html", {"page": page, "year": current_year})


def group_posts(request, slug):
    group = get_object_or_404(Group, slug=slug)
    posts_list = Post.objects.filter(group=group).order_by("-pub_date")
    paginator = Paginator(posts_list, 10)
    page_number = request.GET.get('page')
    page = paginator.get_page(page_number)
    return render(request, "group.html", {"group": group, "page": page})


def profile(request, username):
    # тут тело функции
    return render(request, 'profile.html', {})


def post_view(request, username, post_id):
    # тут тело функции
    return render(request, 'post.html', {})