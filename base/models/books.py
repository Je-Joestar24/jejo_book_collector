"""
Book Model Module

This module defines the Book model which represents the core book information
in the system. Books can have multiple authors and categories through junction tables.
"""

from django.db import models

class Book(models.Model):
    """
    Core model representing books in the system.
    
    Attributes:
        title (str): The title of the book
        description (str): Detailed description of the book
        ratings (float): Book rating (0.0 to 5.0)
        url (str): URL to the book's cover image
        published_date (str): Publication date of the book
        thumbnail (str): URL to the book's thumbnail image
        info_link (str): URL to the book's detailed information
        external_id (str): Unique identifier from external source (e.g., Google Books)
        created_at (datetime): Timestamp of when the book was added
        updated_at (datetime): Timestamp of the last update to the book record
    """
    title = models.CharField(max_length=255)
    description = models.TextField()
    ratings = models.FloatField(default=0.0)
    url = models.URLField()
    published_date = models.CharField(max_length=50)
    thumbnail = models.URLField()
    info_link = models.URLField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    external_id = models.CharField(max_length=255, unique=True, null=True, blank=True)

    class Meta:
        db_table = 'books'
        verbose_name = 'Book'
        verbose_name_plural = 'Books'

    def __str__(self):
        return self.title