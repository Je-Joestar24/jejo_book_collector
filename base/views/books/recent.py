"""
Recent Views Module

This module handles the display of recently viewed books.
It provides paginated access to the user's book viewing history.
"""

from .utils import login_required, render, Recent, Paginator

@login_required
def recent_view(request):
    """
    Display the user's recently viewed books with pagination.
    
    Args:
        request (HttpRequest): The HTTP request object
        
    Returns:
        HttpResponse: Renders recent views page with paginated books
        
    Context:
        recent_views: Paginated recent book views
        page_obj: Current page object
        status: Operation status
        message: Status message
    """
    # Get page number from request
    page_number = request.GET.get('page', 1)
    
    # Get recent views and create paginator
    recent_views = Recent.objects.filter(user=request.user).select_related('book')
    paginator = Paginator(recent_views, 3)  
    
    # Get the current page
    page_obj = paginator.get_page(page_number)
    
    return render(request, 'authed/recent.html', {
        'recent_views': page_obj,
        'page_obj': page_obj,
        'status': 'info',
        'message': 'RECENTLY VIEWED PAGE'
    })