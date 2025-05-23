"""
Book Views Helpers Module

This module provides helper functions for book-related operations.
These functions handle common tasks like book data retrieval,
author/category management, and database operations.

Functions:
- get_random_books: Fetches random books from Google Books API
- get_or_create_author: Manages author creation/retrieval
- get_or_create_category: Manages category creation/retrieval
- save_book_to_db: Saves book data with related authors and categories
- get_collected_books_data: Retrieves user's collected books
- record_recent: Tracks recently viewed books
"""

from .utils import random, requests, Author, Category, transaction, Book, BookAuthor, BookCategory, Collected, Q, api_url, Recent

def get_random_books():
    """
    Fetches random books from Google Books API using predefined search terms.
    
    Returns:
        list: List of book items from Google Books API
    """
    # List of popular search terms to get random books
    search_terms = [
        "fiction", "science", "history", "philosophy", "technology",
        "art", "biography", "poetry", "business", "self-help"
    ]
    
    # Get a random search term
    search_term = random.choice(search_terms)
    
    # Make API request
    params = {
        'q': search_term,
        'maxResults': 10
    }
    
    response = requests.get(api_url, params=params)
    return response.json().get('items', [])

def get_or_create_author(author_name):
    """
    Get or create an author, handling duplicates.
    
    Args:
        author_name (str): Name of the author
        
    Returns:
        Author: Author model instance
    """
    author, created = Author.objects.get_or_create(
        name=author_name.strip(),
        defaults={'name': author_name.strip()}
    )
    return author

def get_or_create_category(category_name):
    """
    Get or create a category, handling duplicates.
    
    Args:
        category_name (str): Name of the category
        
    Returns:
        Category: Category model instance
    """
    category, created = Category.objects.get_or_create(
        name=category_name.strip(),
        defaults={'name': category_name.strip()}
    )
    return category

@transaction.atomic
def save_book_to_db(book_data):
    """
    Save book data to database with authors and categories.
    Uses transaction to ensure data consistency.
    
    Args:
        book_data (dict): Book data from Google Books API
        
    Returns:
        Book: Saved book model instance
    """
    # Extract book information
    volume_info = book_data.get('volumeInfo', {})
    book_id = book_data.get('id')
    
    # Check if book already exists
    if Book.objects.filter(external_id=book_id).exists():
        book = Book.objects.get(external_id=book_id)
        return book
    
    # Create new book
    book = Book(
        title=volume_info.get('title', ''),
        description=volume_info.get('description', ''),
        ratings=volume_info.get('averageRating', 0.0),
        url=volume_info.get('previewLink', ''),
        published_date=volume_info.get('publishedDate', ''),
        thumbnail=volume_info.get('imageLinks', {}).get('thumbnail', ''),
        info_link=volume_info.get('infoLink', ''),
        external_id=book_id
    )
    book.save()
    
    # Handle authors
    authors = volume_info.get('authors', [])
    for author_name in authors:
        author = get_or_create_author(author_name)
        BookAuthor.objects.get_or_create(book=book, author=author)
    
    # Handle categories
    categories = volume_info.get('categories', [])
    for category_name in categories:
        category = get_or_create_category(category_name)
        BookCategory.objects.get_or_create(book=book, category=category)
    
    return book

def get_collected_books_data(user, search_query=''):
    """
    Get collected books data for a user with optional search filtering.
    
    Args:
        user: The user whose collection to fetch
        search_query: Optional search query to filter books
        
    Returns:
        list: List of dictionaries containing book data with authors and categories
    """
    # Base queryset for collected books
    collected_books = Collected.objects.filter(user=user).select_related('book')
    
    if search_query:
        # Search in book title, authors, and categories
        collected_books = collected_books.filter(
            Q(book__title__icontains=search_query) |
            Q(book__bookauthor__author__name__icontains=search_query) |
            Q(book__bookcategory__category__name__icontains=search_query)
        ).distinct()
    
    # Order by most recently collected
    collected_books = collected_books.order_by('-created_at')
    
    # Prepare book data
    books_data = []
    for collected in collected_books:
        book = collected.book
        authors = BookAuthor.objects.filter(book=book).select_related('author')
        categories = BookCategory.objects.filter(book=book).select_related('category')
        
        books_data.append({
            'id': book.id,
            'title': book.title,
            'authors': [author.author.name for author in authors],
            'categories': [category.category.name for category in categories],
            'thumbnail': book.thumbnail,
            'info_link': book.info_link,
            'collected_at': collected.created_at
        })
    
    return books_data

def record_recent(user, book):
    """
    Records a recent book view for the user.
    Ensures only one entry per user-book pair by removing old duplicates.
    
    Args:
        user: The user viewing the book
        book: The book being viewed
    """
    if not user.is_authenticated:
        return  # Skip if user is anonymous

    # Remove old record (if any) for this user and book
    Recent.objects.filter(user=user, book=book).delete()

    # Insert new recent view
    Recent.objects.create(user=user, book=book)
