from django.shortcuts import render

# Create your views here.

def search_book_view(request):
    return render(request, 'authed/searchbook.html')

    