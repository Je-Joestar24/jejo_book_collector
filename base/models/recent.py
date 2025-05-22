"""
Recent Model Module

This module defines the Recent model which tracks books recently viewed by users.
It maintains a history of user interactions with books.
"""

from django.db import models
from .books import Book
from .users import User

class Recent(models.Model):
    """
    Model tracking recently viewed books by users.
    
    Attributes:
        book (Book): Foreign key to the Book model
        user (User): Foreign key to the User model
        viewed_at (datetime): Timestamp of when the book was viewed
    
    Note:
        Records are ordered by viewed_at in descending order to show
        most recent views first.
    """
    book = models.ForeignKey(Book, on_delete=models.CASCADE, db_column='book_id')
    user = models.ForeignKey(User, on_delete=models.CASCADE, db_column='user_id')
    viewed_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'recent'
        verbose_name = 'Recent View'
        verbose_name_plural = 'Recent Views'
        ordering = ['-viewed_at']

    def __str__(self):
        return f"{self.user.username} - {self.book.title}"