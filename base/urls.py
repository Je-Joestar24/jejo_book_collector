
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='books'),
    path('users/',views.users, name='users')
]
