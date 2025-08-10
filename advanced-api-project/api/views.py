from rest_framework import generics, permissions
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from .models import Book
from .serializers import BookSerializer
from .permissions import IsOwnerOrReadOnly
from django_filters import rest_framework as filters
from .filters import BookFilter

class ListView(generics.ListAPIView):
    """
    View to list all books (GET /books/)
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    
    # Filter backends configuration
    filter_backends = [
        filters.DjangoFilterBackend,  # For field filtering
        filters.SearchFilter,                # For search functionality
        filters.OrderingFilter               # For ordering results
    ]
    
    # Filtering setup
    filterset_class = BookFilter
    
    # Search setup (matches the task requirement)
    search_fields = ['title', 'author__name']  # Search by title and author
    
    # Ordering setup
    ordering_fields = ['title', 'publication_year']  # Fields available for ordering
    ordering = ['title']  # Default ordering
class DetailView(generics.RetrieveAPIView):
    """
    View to retrieve a single book (GET /books/<id>/)
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]  # Read-only for all users

class CreateView(generics.CreateAPIView):
    """
    View to create a new book (POST /books/create/)
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]  # Only authenticated users

    def perform_create(self, serializer):
        """
        Custom create logic can be added here
        """
        serializer.save()
    def create(self, request, *args, **kwargs):
        """
        Custom create method with additional validation
        """
        # You can add pre-create validation here
        return super().create(request, *args, **kwargs)

class UpdateView(generics.UpdateAPIView):
    """
    View to update an existing book (PUT /books/<id>/update/)
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]  # Only authenticated users

    def perform_update(self, serializer):
        """
        Custom update logic can be added here
        """
        serializer.save()
    def create(self, request, *args, **kwargs):
        """
        Custom create method with additional validation
        """
        # You can add pre-create validation here
        return super().create(request, *args, **kwargs)
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]

class DeleteView(generics.DestroyAPIView):
    """
    View to delete a book (DELETE /books/<id>/delete/)
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]  # Only authenticated users

    def perform_destroy(self, instance):
        """
        Custom delete logic can be added here
        """
        super().perform_destroy(instance)
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]