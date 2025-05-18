from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def search_book_view(request):
    return render(request, 'authed/searchbook.html')

@login_required
def collection_view(request):
    return render(request, 'authed/collection.html')

@login_required
def book_view(request):
    # Mock book data - replace this with actual API call later
    mock_book = {
        'title': 'The Pragmatic Programmer',
        'authors': ['David Thomas', 'Andrew Hunt'],
        'cover_image': 'https://books.google.com/books/content?id=5wBQEp6ruIAC&printsec=frontcover&img=1&zoom=1&edge=curl&source=gbs_api',
        'categories': ['Programming', 'Software Development', 'Technology'],
        'publisher': 'Addison-Wesley Professional',
        'published_date': 'October 1999',
        'average_rating': 4.5,
        'preview_link': 'https://books.google.com/books?id=5wBQEp6ruIAC&printsec=frontcover&dq=pragmatic+programmer&hl=en&sa=X&ved=0ahUKEwj',
        'description': '''
            <p>This book is filled with practical advice on how to become a better programmer. From understanding the philosophy of pragmatic programming to learning specific techniques and best practices, this comprehensive guide covers everything you need to know.</p>
            
            <p>The authors present their philosophy in a series of numbered tips and anecdotes, each designed to help programmers work more effectively and think differently about their craft. Topics covered include:</p>
            
            <ul>
                <li>The importance of taking responsibility for your work</li>
                <li>Writing flexible, dynamic, and adaptable code</li>
                <li>Avoiding duplicate code and the DRY principle</li>
                <li>Using version control effectively</li>
                <li>Testing strategies and debugging techniques</li>
            </ul>
            
            <p>Whether you're a novice programmer or a seasoned veteran, this book will help you improve your craft and become more productive. The lessons learned here will serve you throughout your programming career.</p>
        ''',
        'language': 'English',
        'isbn': '978-0201616224'
    }
    
    context = {
        'book': mock_book
    }
    
    return render(request, 'authed/viewbook.html', context)