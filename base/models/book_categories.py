from django.db import models
from .books import Book
from .categories import Category

class BookCategory(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, db_column='book_id')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, db_column='category_id')

    class Meta:
        db_table = 'book_categories'
        verbose_name = 'Book Category'
        verbose_name_plural = 'Book Categories'
        unique_together = ('book', 'category')

    def __str__(self):
        return f"{self.book.title} - {self.category.name}"