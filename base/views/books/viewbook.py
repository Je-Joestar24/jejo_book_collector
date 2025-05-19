from .utils import login_required, render, Book, BookAuthor, BookCategory, Recent

@login_required
def view_book(request):
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
        Recent.objects.create(book=book, user=request.user)
        
        context = {
            'book': book_data
        }
        
        return render(request, 'authed/viewbook.html', context)
        
    except Book.DoesNotExist:
        return render(request, 'authed/error.html', {'message': 'Book not found'})