from .utils import login_required, render

@login_required
def collection_view(request):
    return render(request, 'authed/collection.html')