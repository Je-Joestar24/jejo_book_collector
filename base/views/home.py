from django.shortcuts import render

# Create your views here.

test = [
    {'test': 1},
    {'test': 1},
    {'test': 1},
]
def home(request):
    return render(request, 'unauthed/home.html', {'test': test})
