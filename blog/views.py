import django.shortcuts
from .models import Post
from django.utils import timezone


def post_list(request):
    posts=Post.objects.filter(published_date_lte=timezone.now()).order_by(published_date)
    return django.render(request, 'blog/post_list.html', {'posts':posts})


