from rest_framework import generics, permissions
from .models import Book, Author
from .serializers import BookSerializer, AuthorSerializer
from .permissions import IsAdminOrReadOnly

class BookListCreateView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        # You could add custom logic here before saving
        serializer.save()

    def get_queryset(self):
        """
        Optionally filter books by publication year via query parameter
        Example: /api/books/?year=2020
        """
        queryset = Book.objects.all()
        year = self.request.query_params.get('year')
        if year is not None:
            queryset = queryset.filter(publication_year=year)
        return queryset

class BookRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    """
    View to retrieve, update or delete a single book instance.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class AuthorListView(generics.ListAPIView):
    """
    View to list all authors.
    """
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class BookListCreateView(generics.ListCreateAPIView):
    permission_classes = [IsAdminOrReadOnly]  # Changed from previous

class BookRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAdminOrReadOnly]  # Changed from previous