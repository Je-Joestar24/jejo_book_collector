from .utils import login_required, render

@login_required
def profile_view(request):
    user = request.user  # Get the logged-in user

    context = {
        'fullname': user.fullname,
        'username': user.username,
        'email': user.email,
        'id': user.id,
    }

    return render(request, 'authed/profile.html', context)