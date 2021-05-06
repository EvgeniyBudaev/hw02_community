from django.shortcuts import render, get_object_or_404
import datetime as dt

from .models import Post, Group


def index(request):
    latest = Post.objects.order_by("-pub_date")[:11]
    current_year = dt.datetime.now().year
    return render(request, "index.html", {"posts": latest, "year": current_year})


def group_posts(request, slug):
    group = get_object_or_404(Group, slug=slug)
    posts = Post.objects.filter(group=group).order_by("-pub_date")[:12]
    return render(request, "group.html", {"group": group, "posts": posts})