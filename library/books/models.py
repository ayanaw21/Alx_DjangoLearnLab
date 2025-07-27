from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length = 200)
    bio = models.TextField(blank=True)
    birth_date = models.DateField(null =True,blank=True) 

    def __str__(self):
        return self.name
class Genre(models.Model):
    name = models.CharField(max_length = 50,unique = True)
    description = models.TextField(blank = True)
    
    def __str__(self):
        return self.name
class Book(models.Model):
    title = models.CharField(max_length = 50)
    author = models.ForeignKey(Author,on_delete=models.CASCADE,related_name='books')
    genres = models.ManyToManyField(Genre,related_name='books')
    published_date = models.DateField()
    isbn = models.CharField(max_length=13 , unique=True)
    page_count = models.PositiveIntegerField()
    available_copies = models.PositiveIntegerField(default=0)
    def __str__(self):
        return f"{self.title} by {self.author.name}"
    
class BookLoan(models.Model):
    LOAN_STATUS = [
        ('B','Borrowed'),
        ('R','Returned'),
        ('O','Overdue')
    ]
    
    book = models.ForeignKey(Book,on_delete=models.CASCADE,related_name='loans')
    borrower = models.ForeignKey(User,on_delete=models.CASCADE,related_name='loan')
    due_date = models.DateField()
    return_date  = models.DateField(null =True,blank=True)
    status = models.CharField(max_length=1,choices=LOAN_STATUS,default='B')
    
    def __str__(self):
        return f"{self.book.title} loaned to {self.borrower.username}"