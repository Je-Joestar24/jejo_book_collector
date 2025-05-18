from .utils import render, redirect, User, authenticate, login, messages

def login_process(request):
    
    if request.user.is_authenticated:
        return redirect('search_book_view') 

    if request.method == 'POST':
        username_or_email = request.POST.get('username')
        password = request.POST.get('password')
        
        # Try to authenticate with username
        user = authenticate(request, username=username_or_email, password=password)
        
        # If authentication fails, try with email
        if user is None:
            try:
                # Get user by email
                user_obj = User.objects.get(email=username_or_email)
                # Try to authenticate with email
                user = authenticate(request, username=user_obj.username, password=password)
            except User.DoesNotExist:
                user = None
        
        if user is not None:
            login(request, user)
            next_url = request.GET.get('next', '/search/book/')
            return redirect(next_url)
        else:
            messages.error(request, 'Invalid username/email or password')
            return render(request, 'unauthed/login.html', {'error': True})
    
    return render(request, 'unauthed/login.html')