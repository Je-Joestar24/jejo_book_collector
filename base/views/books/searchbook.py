"""
Search Book View Module

This module handles book search functionality using the Google Books API.
It provides features for searching, filtering, and sorting books.
"""

from .utils import login_required, requests, BookAuthor, BookCategory, render, api_url
from .helpers import get_random_books, save_book_to_db

@login_required
def search_book_view(request):
    """
    Handle book search and display with filtering and sorting options.
    
    Args:
        request (HttpRequest): The HTTP request object
        
    Returns:
        HttpResponse: Renders search results page
        
    Features:
        - Random book suggestions when no search query
        - Category filtering
        - Title sorting
        - Author and category information
        - Book details including ratings and links
        
    Context:
        books: List of book data dictionaries
        search_query: Current search query
        category: Selected category filter
        sort_by: Current sort option
        status: Operation status
        message: Status message
    """
    if request.method == 'GET':
        search_query = request.GET.get('q', '')
        category = request.GET.get('category', '')
        sort_by = request.GET.get('sort', '')
        
        if not search_query:
            # Get random books for initial load
            books_data = get_random_books()
        else:
            # Search books based on query
            params = {
                'q': search_query,
                'maxResults': 10
            }
            
            if category:
                params['q'] += f" subject:{category}"
            
            response = requests.get(api_url, params=params)
            books_data = response.json().get('items', [])
        
        # Save books to database and get their IDs
        books = []
        for book_data in books_data:
            book = save_book_to_db(book_data)
            books.append(book)
        
        # Sort books if requested
        if sort_by == 'title':
            books.sort(key=lambda x: x.title)
        
        # Prepare book data with authors and categories
        books_data = []
        for book in books:
            authors = [ba.author.name for ba in BookAuthor.objects.filter(book=book)]
            categories = [bc.category.name for bc in BookCategory.objects.filter(book=book)]
            
            books_data.append({
                'id': book.id,
                'title': book.title,
                'description': book.description,
                'ratings': book.ratings,
                'thumbnail': book.thumbnail,
                'url': book.url,
                'published_date': book.published_date,
                'info_link': book.info_link,
                'authors': authors,
                'categories': categories
            })
        
        context = {
            'books': books_data,
            'search_query': search_query,
            'category': category,
            'sort_by': sort_by,
            'status': 'info',
            'message': 'SEARCH BOOK PAGE'
        }
        
        return render(request, 'authed/searchbook.html', context)
