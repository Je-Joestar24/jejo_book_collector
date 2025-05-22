"""
Collected Model Module

This module defines the Collected model which represents books that users
have added to their collection. It creates a many-to-many relationship
between users and books.
"""

from django.db import models
from .books import Book
from .users import User

class Collected(models.Model):
    """
    Model representing books collected by users.
    
    Attributes:
        book (Book): Foreign key to the Book model
        user (User): Foreign key to the User model
        created_at (datetime): Timestamp of when the book was added to collection
    
    Note:
        The combination of book and user must be unique to prevent
        duplicate entries in a user's collection.
    """
    book = models.ForeignKey(Book, on_delete=models.CASCADE, db_column='book_id')
    user = models.ForeignKey(User, on_delete=models.CASCADE, db_column='user_id')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'collected'
        verbose_name = 'Collected Book'
        verbose_name_plural = 'Collected Books'
        unique_together = ('book', 'user')

    def __str__(self):
        return f"{self.user.username} - {self.book.title}"