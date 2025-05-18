from django.db import models
from .books import Book
from .users import User

class Recent(models.Model):
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