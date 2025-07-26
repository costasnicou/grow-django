from django.shortcuts import render, redirect, get_object_or_404
from .models import BookCategory,Book
# Create your views here.
# views.py
from app.models import VideoCategory
def books_list(request):
    video_categories = VideoCategory.objects.all()
    category = BookCategory.objects.all()
    books= Book.objects.all()
    return render(request, 'books/bookshop.html', {
        'video_categories':video_categories,
        'category': category, 
        'books': books
    })


# def book_detail(request, pk):
#     book = get_object_or_404(Book, pk=pk)
#     return render(request, 'books/book_detail.html', {'book': book})0