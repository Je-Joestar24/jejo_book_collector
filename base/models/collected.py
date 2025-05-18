from django.db import models
from .books import Book
from .users import User

class Collected(models.Model):
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