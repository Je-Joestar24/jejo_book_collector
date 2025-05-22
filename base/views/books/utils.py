"""
Book Views Utilities Module

This module provides common utilities and imports used across book-related views.
It centralizes imports and provides access to necessary components for book management.

Imports:
- Django Components:
  - shortcuts: render
  - auth: login_required decorator
  - conf: settings
  - db: transaction, Q
  - http: JsonResponse
  - paginator: Paginator
- External Libraries:
  - requests: For API calls
  - random: For random book selection
  - json: For JSON handling
- Models:
  - Book: Core book information
  - Author: Book authors
  - Category: Book categories
  - BookAuthor: Book-author relationships
  - BookCategory: Book-category relationships
  - Recent: Recent views tracking
  - Collected: User collections

Constants:
- api_url: Google Books API endpoint from settings
"""

from django.shortcuts import render
from django.contrib.auth.decorators import login_required
import requests
import random
import json
from base.models.books import Book
from base.models.authors import Author
from base.models.categories import Category
from base.models.book_authors import BookAuthor
from base.models.book_categories import BookCategory
from django.conf import settings
from django.db import transaction
from base.models.recent import Recent
from django.db.models import Q
from base.models.collected import Collected
from django.http import JsonResponse
from django.core.paginator import Paginator

api_url = settings.GOOGLE_BOOKS_API_URL