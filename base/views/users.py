from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model, login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required

User = get_user_model()

# Create your views here.
@login_required
def users(request):
    user_list = User.objects.all()
    return render(request, 'users/users.html', {'users': user_list})

def logout_process(request):
    logout(request)
    return redirect('home_view')

@login_required
def profile_view(request):
    return render(request, 'authed/profile.html')

def signup_process(request):
    if request.method == 'POST':
        fullname = request.POST.get('fullname')
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        # Validation
        if password != confirm_password:
            return render(request, 'unauthed/signup.html', {
                'error': 'Passwords do not match'
            })

        # Check if email already exists
        if User.objects.filter(email=email).exists():
            return render(request, 'unauthed/signup.html', {
                'error': 'Email already exists'
            })

        # Check if username already exists
        if User.objects.filter(username=username).exists():
            return render(request, 'unauthed/signup.html', {
                'error': 'Username already exists'
            })

        try:
            # Create new user with hashed password
            user = User.objects.create_user(
                fullname=fullname,
                email=email,
                username=username,
                password=password
            )

            login(request, user)
            
            # Redirect to search book view
            return redirect('search_book_view')
            
        except Exception as e:
            return render(request, 'unauthed/signup.html', {
                'error': 'An error occurred during signup. Please try again.'
            })

    return render(request, 'unauthed/signup.html')

def login_process(request):
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