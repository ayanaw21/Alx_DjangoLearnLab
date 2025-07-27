from django.shortcuts import render
from .models import Author,Librarian,Library,Book
# Create your views here.
from django.http import HttpResponse
from django.views.generic.detail import DetailView

# Create Authors
author1 = Author.objects.create(name="J.K. Rowling")
author2 = Author.objects.create(name="George Orwell")

# Create Books (One-to-Many with Author)
book1 = Book.objects.create(title="Harry Potter", author=author1)
book2 = Book.objects.create(title="1984", author=author2)
book3 = Book.objects.create(title="Animal Farm", author=author2)

# Create Libraries (Many-to-Many with Books)
central_lib = Library.objects.create(name="Central Library")
central_lib.books.add(book1, book2)  # Add multiple books

downtown_lib = Library.objects.create(name="Downtown Library")
downtown_lib.books.add(book1, book3)

# Create Librarians (One-to-One with Library)
Librarian.objects.create(name="Sarah Johnson", library=central_lib)
Librarian.objects.create(name="Michael Brown", library=downtown_lib)
def index(request):
    return HttpResponse("Hello, world. You are at relation index ")
def list_books(request):
    books = Book.objects.all()
    
    return render(request,"list_books.html",{"books":books})

class LibraryDetailView(DetailView):
    model = Library
    template_name = 'library_detail.html'
    context_object_name = 'library'

    
    