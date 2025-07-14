from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='homepage' ),
    path('stories/<slug:slug>/', views.coach_story_detail, name='coach_story_detail'), 
    path('category/<slug:slug>/', views.video_category_detail, name='video_category_detail'), 
    # path('stories/<slug:slug>/', views.coach_story_detail, name='coach_story_detail'),
]