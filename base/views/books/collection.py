from .utils import login_required, render, Collected, Book, json, JsonResponse
from .helpers import get_collected_books_data

search_query = ''

@login_required
def collection_view(request):
    # Get search query if any
    search_query = request.GET.get('search', '')
    
    # Get books data using the helper function
    books_data = get_collected_books_data(request.user, search_query)
    
    return render(request, 'authed/collection.html', {
        'books': books_data,
        'search_query': search_query
    })

@login_required
def collect_book(request):
    if request.method == 'POST':
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
    if request.method == 'POST':
        book_id = request.POST.get('book_id')
        
        try:
            book = Book.objects.get(id=book_id)
            collected = Collected.objects.filter(user=request.user, book=book)
            
            if collected.exists():
                collected.delete()
                # Get updated books data after removal
                books_data = get_collected_books_data(request.user)
                return render(request, 'authed/collection.html', {
                    'books': books_data,
                    'search_query': search_query
                })
                
        except Book.DoesNotExist:
            return JsonResponse({
                'status': 'error',
                'message': 'Book not found'
            }, status=404)
    
    return render(request, 'authed/collection.html', {
        'books': books_data,
        'search_query': search_query
    })
    