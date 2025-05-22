"""
Author Model Module

This module defines the Author model which represents book authors in the system.
Authors are linked to books through the BookAuthor junction table.
"""

from django.db import models

class Author(models.Model):
    """
    Author model representing book authors in the system.
    
    Attributes:
        name (str): The full name of the author
        created_at (datetime): Timestamp of when the author was added
        updated_at (datetime): Timestamp of the last update to the author record
    """
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'authors'
        verbose_name = 'Author'
        verbose_name_plural = 'Authors'

    def __str__(self):
        return self.name