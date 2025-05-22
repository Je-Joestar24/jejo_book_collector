from .utils import login_required, render, Recent

@login_required
def recent_view(request):
    recent_views = Recent.objects.filter(user=request.user).select_related('book')
    return render(request, 'authed/recent.html', {
        'recent_views': recent_views,
        'status': 'info',
        'message': 'RECENTLY VIEWED PAGE'
    })