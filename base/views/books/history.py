from .utils import login_required, render


@login_required
def history_view(request):
    return render(request, 'authed/history.html')