"""
User Model Module

This module defines a custom User model that extends Django's AbstractUser.
It adds additional fields for user profile information while maintaining
all the standard Django user functionality.
"""

from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    """
    Custom user model extending Django's AbstractUser.
    
    Attributes:
        fullname (str): User's full name
        created_at (datetime): Timestamp of when the user account was created
        updated_at (datetime): Timestamp of the last update to the user profile
    
    Inherited Attributes:
        username (str): Unique username for login
        email (str): User's email address
        password (str): Hashed password
        is_active (bool): Whether the account is active
        is_staff (bool): Whether the user has staff privileges
        is_superuser (bool): Whether the user has superuser privileges
        date_joined (datetime): When the user account was created
        last_login (datetime): When the user last logged in
    """
    fullname = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'users'
        verbose_name = 'User'
        verbose_name_plural = 'Users'

    def __str__(self):
        return self.username