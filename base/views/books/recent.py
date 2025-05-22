from .utils import login_required, render, Recent, Paginator

@login_required
def recent_view(request):
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