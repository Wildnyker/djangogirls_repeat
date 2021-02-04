from django.shortcuts import render
from .models import Post #21 to use out model in view
from django.utils import timezone

# Create your views here.
#22 create post_list view

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    """we get all published posts and sort them by date/time"""
    return render(request, "blog/post_list.html", {'posts':posts})
"""that takes request and will return the value it gets from calling another 
function render that will render (put together) our template blog/post_list.html"""


#23 create template for your pages
#24 create post_list.html in templates/blog

