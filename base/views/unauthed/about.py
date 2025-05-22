from django.shortcuts import render, redirect

def about_view(request):
    if request.user.is_authenticated:
        return redirect('search_book_view') 

    return render(request, 'unauthed/about.html', {
        'status': 'info',
        'message': 'ABOUT PAGE'
        })