"""
Category Model Module

This module defines the Category model which represents book categories or genres
in the system. Categories are linked to books through the BookCategory junction table.
"""

from django.db import models

class Category(models.Model):
    """
    Model representing book categories or genres.
    
    Attributes:
        name (str): The name of the category/genre
        created_at (datetime): Timestamp of when the category was added
        updated_at (datetime): Timestamp of the last update to the category record
    """
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'categories'
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name