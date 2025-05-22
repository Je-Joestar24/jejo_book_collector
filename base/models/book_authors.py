"""
BookAuthor Model Module

This module defines the BookAuthor model which serves as a junction table
between books and authors, enabling many-to-many relationships between
books and their authors.
"""

from django.db import models
from .books import Book
from .authors import Author

class BookAuthor(models.Model):
    """
    Junction model connecting books and authors in a many-to-many relationship.
    
    Attributes:
        book (Book): Foreign key to the Book model
        author (Author): Foreign key to the Author model
    
    Note:
        The combination of book and author must be unique to prevent
        duplicate author entries for the same book.
    """
    book = models.ForeignKey(Book, on_delete=models.CASCADE, db_column='book_id')
    author = models.ForeignKey(Author, on_delete=models.CASCADE, db_column='author_id')

    class Meta:
        db_table = 'book_authors'
        verbose_name = 'Book Author'
        verbose_name_plural = 'Book Authors'
        unique_together = ('book', 'author')

    def __str__(self):
        return f"{self.book.title} - {self.author.name}"