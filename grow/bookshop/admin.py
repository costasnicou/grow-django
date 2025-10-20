from django.contrib import admin

# Register your models here.
# admin.py
from .models import Book, BookCategory,Author

admin.site.register(Book)
admin.site.register(BookCategory)
admin.site.register(Author)