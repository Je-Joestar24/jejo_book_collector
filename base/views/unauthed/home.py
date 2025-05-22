from django.shortcuts import render, redirect

def home_view(request):
    if request.user.is_authenticated:
        return redirect('search_book_view') 
        
    return render(request, 'unauthed/home.html', {
        'status': 'info',
        'message': 'HOME PAGE'
        })