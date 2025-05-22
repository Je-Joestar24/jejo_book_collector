from .utils import login_required, render, Collected, Book, json, JsonResponse, Paginator
from .helpers import get_collected_books_data

search_query = ''

@login_required
def collection_view(request):
    # Get search query if any
    search_query = request.GET.get('search', '')
    page_number = request.GET.get('page', 1)
    
    # Get books data using the helper function
    books_data = get_collected_books_data(request.user, search_query)
    
    # Create paginator
    paginator = Paginator(books_data, 4)  # Show 10 books per page
    page_obj = paginator.get_page(page_number)
    
    return render(request, 'authed/collection.html', {
        'books': page_obj,
        'search_query': search_query,
        'status': 'info',
        'message': 'COLLECTION PAGE',
        'paginator': paginator,
        'page_obj': page_obj
    })

@login_required
def collect_book(request):
    if request.method == 'PUT':
        data = json.loads(request.body)
        book_id = data.get('book_id')
        
        try:
            book = Book.objects.get(id=book_id)
            
            # Check if already collected
            if not Collected.objects.filter(user=request.user, book=book).exists():
                Collected.objects.create(user=request.user, book=book)
                return JsonResponse({'status': 'success', 'message': 'Book added to collection'})
            else:
                return JsonResponse({'status': 'info', 'message': 'Book already in collection'})
                
        except Book.DoesNotExist:
            return JsonResponse({'status': 'error', 'message': 'Book not found'}, status=404)
    
    return JsonResponse({'status': 'error', 'message': 'Invalid request'}, status=400)

@login_required
def remove_book(request):
    # Get common parameters
    page_number = int(request.GET.get('page', request.POST.get('page', 1)))
    search_query = request.GET.get('search', request.POST.get('search', ''))
    
    if request.method == 'POST':
        book_id = request.POST.get('book_id')
        
        try:
            book = Book.objects.get(id=book_id)
            collected = Collected.objects.filter(user=request.user, book=book)
            
            if collected.exists():
                collected.delete()
                # Get updated books data after removal
                books_data = get_collected_books_data(request.user, search_query)
                
                # Create paginator
                paginator = Paginator(books_data, 4) 
                
                # If current page is empty after deletion, go to previous page
                if page_number > paginator.num_pages:
                    page_number = max(1, paginator.num_pages)
                
                page_obj = paginator.get_page(page_number)
                
                return render(request, 'authed/collection.html', {
                    'books': page_obj,
                    'search_query': search_query,
                    'status': 'success',
                    'message': 'Success removing book',
                    'paginator': paginator,
                    'page_obj': page_obj
                })
                
        except Book.DoesNotExist:
            return JsonResponse({
                'status': 'error',
                'message': 'Book not found'
            }, status=404)
    
    # Handle GET request (pagination)
    books_data = get_collected_books_data(request.user, search_query)
    paginator = Paginator(books_data, 4)
    
    # If current page is empty, go to previous page
    if page_number > paginator.num_pages:
        page_number = max(1, paginator.num_pages)
    
    page_obj = paginator.get_page(page_number)
    
    return render(request, 'authed/collection.html', {
        'books': page_obj,
        'search_query': search_query,
        'status': 'success',
        'message': 'COLLECTION PAGE',
        'paginator': paginator,
        'page_obj': page_obj
    })
    