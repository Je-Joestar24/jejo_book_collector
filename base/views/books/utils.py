from django.shortcuts import render
from django.contrib.auth.decorators import login_required
import requests
import random
from ...models.books import Book
from ...models.authors import Author
from ...models.categories import Category
from ...models.book_authors import BookAuthor
from ...models.book_categories import BookCategory
from django.conf import settings
from django.db import transaction
from ...models.recent import Recent

api_url = settings.GOOGLE_BOOKS_API_URL