from django.shortcuts import render
from app.models import VideoCategory
# Create your views here.
from django.shortcuts import render, get_object_or_404
from .models import Post

def post_list(request):
    video_categories = VideoCategory.objects.all()
    posts = Post.objects.filter(published=True).order_by('-created_at')
    return render(request, 'blog/post_list.html', {
        'posts': posts,
        'video_categories':video_categories,
    })

def post_detail(request, slug):
    video_categories = VideoCategory.objects.all()
    post = get_object_or_404(Post, slug=slug, published=True)
    return render(request, 'blog/post_detail.html', {
        'post': post,
        'video_categories':video_categories,
    })
