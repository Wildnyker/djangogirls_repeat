from django.shortcuts import render
from .models import Post #21 to use out model in view
from django.utils import timezone
from django.shortcuts import render, get_object_or_404 #28 for post_detail
from .forms import PostForm #35 to add our form
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
"""There we created the css connections to bootstrap and our own css files"""
#25 then we creata base.html to get the template for other pages


#29 creating post_detail

def post_detail(request, pk):
    """remember as we need pk (number of post of databese we call it as well)"""
    post = get_object_or_404(Post, pk=pk)
    """checks if object exists if not returns 404 page"""
    return render(request, 'blog/post_detail.html', {"post":post})

#30 create post_detail html


#37 creating post_new
from django.shortcuts import redirect #  - to redirect one page to other with fetched data from form
def post_new(request):
    if request.method == "POST": # if we already fetched info from form then do next:
        form = PostForm(request.POST) # form data = to info from POST
        if form.is_valid(): # if everything is valid do next
            post = form.save(commit=False) # we do not want to commit it right away becouse we want django to add some data
            post.author = request.user # data about author which = to logged user
            post.published_date = timezone.now() # date of publishing = to timezone.now()
            post.save() # now we save the gathered date
            return redirect('post_detail', pk=post.pk) # now redirect to a page of new post
    else:
        form = PostForm() # if nothing was commited work like simple form
    return render(request, 'blog/post_edit.html', {'form': form})

#38 Now lets create editing - first go to post_detail.html to add button to edit mode
#remember we have already created post_edit html it works for new posts and editing


#41 creating post_edit
def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    """checks if object exists if not returns 404 page"""
    if request.method == "POST":
        form = PostForm(request.POST, instance=post) # all this works almost like in post new
        #but it takes instance of post(the data stored in this post before)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})


#43 go to base.html to add {% if user.is_authenticated %}




