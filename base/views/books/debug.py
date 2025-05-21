from .utils import Book, login_required, render

# Create your views here.
@login_required
def books(request):
    user_list = Book.objects.get(id=97)
    return render(request, 'users/books.html', {'users': user_list})