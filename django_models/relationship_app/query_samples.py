from .models import Author,Book,Library,Librarian

def run_queries():
    author_name = "George Orwell"
    library_name = "Central Library"
    try :
        author = Author.objects.get(name = author_name)
        books_by_author = Book.objects.filter(author  = author)
        print(f"Books by {author_name} : ")
        for book in books_by_author:
            print(f"- {book.title}")
    except Author.DoesNotExist:
        print(f"No author found with name {author_name}")
    try :
        library = Library.object.get(name = library_name )
        print(f"Books in library {library_name}")
        for book in library.books.all:
            print(f"- {book.title}")
    except Library.DoesNotExits:
        print(f"No library found with name {library_name}")
        library =  None
    try :
        librarian = Librarian.objects.get(library = library)
        print(f"Librarian for library {library_name} : {librarian.name}")
    except Librarian.DoesNotExist:
        print(f"No librarian assigned to library {library_name}")


if __name__ == "__main__":
    run_queries()
        
    