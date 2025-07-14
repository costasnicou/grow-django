from django.contrib import admin

# Register your models here.
from .models import CoachStory
from .models import Video, VideoCategory, Author


@admin.register(CoachStory)
class CoachStoryAdmin(admin.ModelAdmin):
    list_display = ('coach_name', 'slug')  # show slug in admin
    prepopulated_fields = {'slug': ('coach_name',)}  # auto-fill from name in admin

@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    list_display = ('title','category', 'author', 'added_on')
    list_filter = ('category', 'author')

@admin.register(VideoCategory)
class VideoCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name',)
