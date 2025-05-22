from .utils import login_required, render
from django.contrib import messages

@login_required
def profile_view(request):
    user = request.user  # Get the logged-in user
    
    if request.method == 'POST':
        # Handle profile update
        fullname = request.POST.get('fullname')
        email = request.POST.get('email')
        username = request.POST.get('username')
        
        try:
            user.fullname = fullname
            user.email = email
            user.username = username
            user.save()
            
            messages.success(request, 'Profile updated successfully')
        except Exception as e:
            messages.error(request, str(e))
            
        return render(request, 'authed/profile.html', {
            'fullname': user.fullname,
            'username': user.username,
            'email': user.email,
            'id': user.id,
            'status': 'success',
            'message': 'PROFILE UPDATED'
        })

    # GET request - show profile
    context = {
        'fullname': user.fullname,
        'username': user.username,
        'email': user.email,
        'id': user.id,
        'status': 'info',
        'message': 'PROFILE PAGE'
    }

    return render(request, 'authed/profile.html', context)