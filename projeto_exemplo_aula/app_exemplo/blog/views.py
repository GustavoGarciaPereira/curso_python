from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from .models import Post, Comment
from .forms import CommentForm

def post_list(request):
    posts = Post.objects.all()
    return render(request, 'post_list.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    comments = post.comments.all()
    form = CommentForm()
    
    print("ssssss")
    return render(request, 'post_detail.html', {'post': post, 'comments': comments, 'form': form})

@login_required
def add_comment(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.post = post
            comment.save()
            return redirect('post_detail', pk=pk)
    return redirect('post_detail', pk=pk)

@login_required
def delete_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.user == post.author or request.user.is_superuser:
        post.delete()
        return redirect('post_list')
    else:
        return HttpResponseForbidden("Você não tem permissão para deletar este post.")


from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Post
from .forms import PostForm

@login_required
def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('post_list')
    else:
        form = PostForm()
    print("ssssssssss")
    return render(request, 'create_post.html', {'form': form})