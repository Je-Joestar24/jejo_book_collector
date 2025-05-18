from django.shortcuts import render, redirect

# Create your views here.

def home_view(request):
    if request.user.is_authenticated:
        return redirect('search_book_view') 
        
    return render(request, 'unauthed/home.html')

def about_view(request):
    if request.user.is_authenticated:
        return redirect('search_book_view') 

    return render(request, 'unauthed/about.html')
    
def login_view(request):
    if request.user.is_authenticated:
        return redirect('search_book_view') 

    return render(request, 'unauthed/login.html')
    
def signup_view(request):
    if request.user.is_authenticated:
        return redirect('search_book_view') 

    return render(request, 'unauthed/signup.html')