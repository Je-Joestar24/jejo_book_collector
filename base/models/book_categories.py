"""
BookCategory Model Module

This module defines the BookCategory model which serves as a junction table
between books and categories, enabling many-to-many relationships between
books and their categories/genres.
"""

from django.db import models
from .books import Book
from .categories import Category

class BookCategory(models.Model):
    """
    Junction model connecting books and categories in a many-to-many relationship.
    
    Attributes:
        book (Book): Foreign key to the Book model
        category (Category): Foreign key to the Category model
    
    Note:
        The combination of book and category must be unique to prevent
        duplicate category entries for the same book.
    """
    book = models.ForeignKey(Book, on_delete=models.CASCADE, db_column='book_id')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, db_column='category_id')

    class Meta:
        db_table = 'book_categories'
        verbose_name = 'Book Category'
        verbose_name_plural = 'Book Categories'
        unique_together = ('book', 'category')

    def __str__(self):
        return f"{self.book.title} - {self.category.name}"