from django.db import models
from django.utils.text import slugify
from django_ckeditor_5.fields import CKEditor5Field
class Post(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, blank=True)
    content = CKEditor5Field('Content', config_name='extends')  # or 'default'
    image = models.ImageField(upload_to='blog_images/', blank=True, null=True)
    author = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    published = models.BooleanField(default=False)
    featured = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title