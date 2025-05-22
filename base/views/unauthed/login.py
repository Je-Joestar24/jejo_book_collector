from django.shortcuts import render, redirect
    
def login_view(request):
    if request.user.is_authenticated:
        return redirect('search_book_view') 

    return render(request, 'unauthed/login.html', {
        'status': 'info',
        'message': 'LOGIN NOW!'
    })