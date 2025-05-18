from .utils import login_required, logout, redirect

@login_required
def logout_process(request):
    logout(request)
    return redirect('home_view')