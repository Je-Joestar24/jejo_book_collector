from django.db import models
from .books import Book
from .authors import Author

class BookAuthor(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, db_column='book_id')
    author = models.ForeignKey(Author, on_delete=models.CASCADE, db_column='author_id')

    class Meta:
        db_table = 'book_authors'
        verbose_name = 'Book Author'
        verbose_name_plural = 'Book Authors'
        unique_together = ('book', 'author')

    def __str__(self):
        return f"{self.book.title} - {self.author.name}"