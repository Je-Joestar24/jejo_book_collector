from django.shortcuts import render

# Create your views here.

def users(request):
    return render(request, 'users/users.html')


def profile_view(request):
    return render(request, 'authed/profile.html')