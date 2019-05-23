import django.shortcuts
def post_list(request):
    return django.shortcuts.render(request, 'blog/post_list.html', {})


