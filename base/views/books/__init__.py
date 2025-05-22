"""
Book Views Package Initialization

This module imports and exposes all book-related view functions.
These views handle the core functionality of the book collection system:

Imported Views:
- searchbook: Book search and discovery functionality
- viewbook: Detailed book viewing and recent tracking
- collection: User's book collection management
- recent: Recently viewed books tracking

Each view is protected by authentication and includes proper
error handling and data validation.
"""

from .searchbook import *
from .viewbook import *
from .collection import *
from .recent import *