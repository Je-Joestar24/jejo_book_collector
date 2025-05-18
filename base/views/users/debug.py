from .utils import login_required, render, User

# Create your views here.
@login_required
def users(request):
    user_list = User.objects.all()
    return render(request, 'users/users.html', {'users': user_list})