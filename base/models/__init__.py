"""
Models Package Initialization

This module imports and exposes all model classes from the base application.
The models are organized into separate files for better maintainability and
follow a modular structure for the book collection system.

Imported Models:
- Author: Represents book authors
- BookAuthor: Junction table for books and authors
- BookCategory: Junction table for books and categories
- Book: Core book information
- Category: Book categories/genres
- Collected: User's book collection
- Recent: Recently viewed books
- User: Custom user model
"""

from .authors import *
from .book_authors import *
from .book_categories import *
from .books import *
from .categories import *
from .collected import *
from .recent import *
from .users import *