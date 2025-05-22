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