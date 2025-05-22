"""
View Book Module

This module handles the detailed view of individual books.
It provides comprehensive book information and tracks recent views.
"""

from .utils import login_required, render, Book, BookAuthor, BookCategory, Recent
from .helpers import record_recent

@login_required
def view_book(request):
    """
    Display detailed information about a specific book.
    
    Args:
        request (HttpRequest): The HTTP request object with book ID
        
    Returns:
        HttpResponse: Renders book details page or error page
        
    Features:
        - Comprehensive book information
        - Author and category details
        - Recent view tracking
        - Error handling for invalid/missing books
        
    Context:
        book: Dictionary containing book details
        status: Operation status
        message: Status message with book title
    """
    book_id = request.GET.get('id')
    
    if not book_id:
        # Handle case when no ID is provided
        return render(request, 'authed/error.html', {'message': 'Book ID is required'})
    
    try:
        # Get the book from database
        book = Book.objects.get(id=book_id)
        
        # Get related authors - Modified to use select_related for better performance
        authors = BookAuthor.objects.select_related('author').filter(book=book)
        author_names = [ba.author.name for ba in authors]
        
        # Get related categories - Modified to use select_related for better performance
        categories = BookCategory.objects.select_related('category').filter(book=book)
        category_names = [bc.category.name for bc in categories]
        
        # Prepare book data for template
        book_data = {
            'title': book.title,
            'authors': author_names,  # Now using the list of author names
            'cover_image': book.thumbnail,
            'categories': category_names,  # Now using the list of category names
            'published_date': book.published_date,
            'average_rating': book.ratings,
            'preview_link': book.url,
            'description': book.description,
            'info_link': book.info_link
        }
        
        # Record this view in recent views
        record_recent(book=book, user=request.user)
        
        context = {
            'book': book_data,
            'status': 'info',
            'message': f'Viewing {book_data["title"]}'
        }
        
        return render(request, 'authed/viewbook.html', context)
        
    except Book.DoesNotExist:
        return render(request, 'authed/error.html', {'message': 'Book not found'})