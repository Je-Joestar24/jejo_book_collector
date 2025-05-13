from django.shortcuts import render

# Create your views here.

def home_view(request):
    return render(request, 'unauthed/home.html')

def about_view(request):
    return render(request, 'unauthed/about.html')
    
def login_view(request):
    return render(request, 'unauthed/login.html')
    
def signup_view(request):
    return render(request, 'unauthed/signup.html')