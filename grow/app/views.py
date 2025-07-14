from django.shortcuts import render, redirect, get_object_or_404
from .models import CoachStory
from .models import Video, VideoCategory, Author
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from urllib.parse import urlencode

# Create your views here.
def homepage(request):

    stories = CoachStory.objects.all()
    video_categories = VideoCategory.objects.all()
    return render(request, 'app/homepage.html',{
        'video_categories':video_categories,
        'stories':stories,
    })

def coach_story_detail(request, slug):
    video_categories = VideoCategory.objects.all()
    story = get_object_or_404(CoachStory, slug=slug)
    is_coach_story=True
    return render(request, 'app/stories/story.html', {
        'story': story,
        'video_categories':video_categories,
        'is_coach_story':is_coach_story,
    })

def video_category_detail(request, slug):
    category = get_object_or_404(VideoCategory, slug=slug)
    video_categories = VideoCategory.objects.all()
    authors = category.authors.all()

    author_id = request.GET.get('author')
    videos = Video.objects.filter(category=category).select_related('author', 'category')

    if author_id:
        videos = videos.filter(author__id=author_id)

    # PAGINATION
    paginator = Paginator(videos, 12)  # 12 videos per page
    page = request.GET.get('page')

    try:
        videos_page = paginator.page(page)
    except PageNotAnInteger:
        videos_page = paginator.page(1)
    except EmptyPage:
        videos_page = paginator.page(paginator.num_pages)

    # Build querystring without the 'page' param
    query_params = request.GET.copy()
    query_params.pop('page', None)
    querystring = urlencode(query_params)


    is_video_category = True

    return render(request, 'app/category.html', {
        'category': category,
        'video_categories': video_categories,
        'videos': videos_page,
        'is_video_category': is_video_category,
        'authors': authors,
        'selected_author_id': int(author_id) if author_id else None,
        'paginator': paginator,
        'page_obj': videos_page,  # for built-in pagination templates
        'querystring': querystring,
    })