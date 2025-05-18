
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home_view'),
    path('about/', views.about_view, name='about_view'),
    path('login/', views.login_view, name='login_view'),
    path('signup/', views.signup_view, name='signup_view'),
    path('search/book/', views.search_book_view, name='search_book_view'),
    path('collection/', views.collection_view, name='collection_view'),
    path('book/view/', views.book_view, name='book_view'),
    path('profile/', views.profile_view, name='profile_view'),
    # AUTHS
    path('auth/signup/', views.signup_process, name='signup'),
    path('auth/login/', views.login_process, name='login'),
    path('auth/logout/', views.logout_process, name='logout'),
    path('user/', views.users, name='user')
]
