from django.db import models
from django_ckeditor_5.fields import CKEditor5Field
from urllib.parse import urlparse, parse_qs

# Create your models here.
class CoachStory(models.Model):
    coach_name = models.CharField(max_length=100)
    coach_img = models.ImageField(default='restaurant_default.jpg',upload_to='restaurant_images')
    story = CKEditor5Field('Story', config_name='default', blank=True)
    slug = models.SlugField(unique=True, blank=True)  # <-- new

    def __str__(self):
        return self.coach_name

    def save(self, *args, **kwargs):
        if not self.slug:
            # Auto-generate slug from name
            self.slug = slugify(self.coach_namename)
        super().save(*args, **kwargs)



class VideoCategory(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name


class Author(models.Model):
    name = models.CharField(max_length=100)
    categories = models.ManyToManyField(VideoCategory, related_name='authors')

    def __str__(self):
        return self.name


class Video(models.Model):
    title = models.CharField(max_length=200, default="Untitled Video")
    youtube_url = models.URLField()
    category = models.ForeignKey(VideoCategory, on_delete=models.CASCADE, related_name='videos')
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='videos')
    added_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def get_youtube_embed_url(self):
        parsed_url = urlparse(self.youtube_url)
        if 'youtube.com' in parsed_url.netloc:
            video_id = parse_qs(parsed_url.query).get('v')
            if video_id:
                return f"https://www.youtube.com/embed/{video_id[0]}"
        elif 'youtu.be' in parsed_url.netloc:
            return f"https://www.youtube.com/embed{parsed_url.path}"
        return self.youtube_url

    def clean(self):
        # Optional: Ensure the selected author is linked to the selected category
        if self.author and self.category and not self.author.categories.filter(id=self.category.id).exists():
            from django.core.exceptions import ValidationError
            raise ValidationError("Selected author is not assigned to this category.")