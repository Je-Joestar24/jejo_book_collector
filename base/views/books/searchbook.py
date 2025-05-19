from .utils import login_required, requests, BookAuthor, BookCategory, render, api_url
from .helpers import get_random_books, save_book_to_db

@login_required
def search_book_view(request):
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
            'sort_by': sort_by
        }
        
        return render(request, 'authed/searchbook.html', context)
