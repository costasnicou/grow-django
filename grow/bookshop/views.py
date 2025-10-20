from django.shortcuts import render, redirect, get_object_or_404
from .models import BookCategory,Book
# Create your views here.
# views.py
from app.models import VideoCategory
def books_list(request):
    video_categories = VideoCategory.objects.all()
    book_categories = BookCategory.objects.all()
    is_booklist = True
    category = BookCategory.objects.all()
    books= Book.objects.all()
    featured_books = Book.objects.filter(featured=True).order_by('-created_at')[1:]
    star_book = Book.objects.filter(featured=True).order_by('-created_at').first()
    personaldev_books = Book.objects.filter(category__name='Personal Development',featured=False)[:8]
    timeprod_books = Book.objects.filter(category__name='Time Management & Productivity')[:8]
    return render(request, 'books/bookshop.html', {
        'video_categories':video_categories,
        'book_categories':book_categories,
        'category': category, 
        'books': books,
        'featured_books':featured_books,
        'star_book':star_book,
        'is_booklist':is_booklist,
        'personaldev_books':personaldev_books,
        'timeprod_books':timeprod_books,
    })


# def book_detail(request, pk):
#     book = get_object_or_404(Book, pk=pk)
#     return render(request, 'books/book_detail.html', {'book': book})0