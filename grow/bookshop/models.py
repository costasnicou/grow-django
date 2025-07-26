from django.db import models
from django.utils.text import slugify

class BookCategory(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name


class Author(models.Model):
    name       = models.CharField(max_length=100, unique=True)
    slug       = models.SlugField(unique=True, blank=True)
    # link authors to categories:
    categories = models.ManyToManyField(
        BookCategory,
        related_name='authors',
        blank=True,
        help_text="Select the categories this author writes in"
    )

    def save(self, *args, **kwargs):
        # auto-populate slug on first save
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class Book(models.Model):
    title        = models.CharField(max_length=200)
    cover_image  = models.ImageField(upload_to='book_covers/')
    amazon_link  = models.URLField()
    featured     = models.BooleanField(default=False)
    # each book belongs to exactly one category...
    category     = models.ForeignKey(
        BookCategory,
        on_delete=models.CASCADE,
        related_name='books'
    )
    # ...and to exactly one author
    author = models.ForeignKey(
        Author,
        null=True,      # ← allow NULLs
        blank=True,     # ← allow blank in forms
        on_delete=models.CASCADE,
        related_name='books'
    )
    created_at   = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title