from django.db import models
from books.models import books

class borrow_logs(models.Model):
    

    book = models.ForeignKey(books, on_delete=models.CASCADE, related_name='borrow_logs')
    borrower_name = models.CharField(max_length=100)
    date_borrowed = models.DateTimeField(auto_now_add=True)
    date_returned = models.DateTimeField(null=True, blank=True)
    is_returned = models.BooleanField(default=False)

    def __str__(self):
        return f"Borrow Log #{self.id} - {self.book.title} by {self.borrower_name}"