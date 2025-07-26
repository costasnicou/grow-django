from django.shortcuts import render
from app.models import VideoCategory
# Create your views here.
from django.shortcuts import render, get_object_or_404
from .models import Post
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def post_list(request):
    video_categories = VideoCategory.objects.all()
    post_list = Post.objects.filter(published=True).order_by('-created_at')

    paginator = Paginator(post_list, 5)  # 5 posts per page
    page_number = request.GET.get('page')

    try:
        posts = paginator.page(page_number)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

    return render(request, 'blog/post_list.html', {
        'posts': posts,
        'video_categories': video_categories,
    })

def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug, published=True)
    video_categories = VideoCategory.objects.all()
    absolute_image_url = None
    if post.image:
        absolute_image_url = request.build_absolute_uri(post.image.url)
   
    return render(request, 'blog/post_detail.html', {
        'post': post,
        'video_categories':video_categories,
        'absolute_image_url': absolute_image_url,
    })
