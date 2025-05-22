
from django.urls import path
from . import views

urlpatterns = [
    # VIEWS
    path('', views.home_view, name='home_view'),
    path('about/', views.about_view, name='about_view'),
    path('login/', views.login_view, name='login_view'),
    path('signup/', views.signup_view, name='signup_view'),
    path('profile/', views.profile_view, name='profile_view'),
    # BOOKS
    path('search/book/', views.search_book_view, name='search_book_view'),
    path('collection/', views.collection_view, name='collection_view'),
    path('collection/collect/', views.collect_book, name='collect_book'),
    path('collection/remove/', views.remove_book, name='remove_book'),
    path('book/view/', views.view_book, name='book_view'),
    path('recent/', views.recent_view, name='recent_view'),
    # AUTHS
    path('auth/signup/', views.signup_process, name='signup'),
    path('auth/login/', views.login_process, name='login'),
    path('auth/logout/', views.logout_process, name='logout'),
]
