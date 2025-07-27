from django.shortcuts import render

# Create your views here.
from books.models import Author, Genre, Book
from datetime import date
from django.contrib.auth.models import User
from django.db.models import Count

# Create authors
author1 = Author.objects.create(name="J.K. Rowling", bio="British author", birth_date="1965-07-31")
author2 = Author.objects.create(name="George Orwell", bio="English novelist", birth_date="1903-06-25")

# Create genres
fiction = Genre.objects.create(name="Fiction", description="Imaginary stories")
fantasy = Genre.objects.create(name="Fantasy", description="Magic and supernatural")
dystopian = Genre.objects.create(name="Dystopian", description="Future oppressive societies")

# Create books
book1 = Book.objects.create(
    title="Harry Potter and the Philosopher's Stone",
    author=author1,
    published_date="1997-06-26",
    isbn="9780747532743",
    page_count=223,
    available_copies=5
)
book1.genres.add(fiction, fantasy)  # Many-to-many relationship

book2 = Book.objects.create(
    title="1984",
    author=author2,
    published_date="1949-06-08",
    isbn="9780451524935",
    page_count=328,
    available_copies=3
)
book2.genres.add(dystopian, fiction)

# two methods using author instance and instance

books_by_rowling =  author1.books.all()
books_by_rowling_ = Book.objects.filter(author__name = 'J.K. Rowling')


fantasy_books = fantasy.books.all();
fantasy_books_ = Book.objects.filter(genres__name = 'Fantasy')

books_after_1990 = Book.objects.filter(published_date__year__gt=1990)


harry_potter = Book.objects.get(title__icontains = 'Harry Potter')
borrowers = User.objects.filter(loans_book = harry_potter).distinct()

# for given users find borrowed books

user = User.objects.first() # ger any user
borrowed_books = Book.objects.filter(loans__borrower = user).distinct()

#never borrowed book list
never_borrowed = Book.objects.exclude(loans__status = "B")

#find authors who has more than 3 books in the library

authors_with_many_books  = Author.objects.annotate(
    book_count = Count("books")
).filter(book_count__gt = 3)

print (authors_with_many_books)

