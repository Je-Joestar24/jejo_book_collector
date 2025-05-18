from .utils import redirect, render, User, login

def signup_process(request):
    
    if request.user.is_authenticated:
        return redirect('search_book_view') 

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
