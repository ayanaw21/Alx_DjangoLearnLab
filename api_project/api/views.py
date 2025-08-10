from rest_framework import generics, viewsets, status
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated  
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from .models import Book
from .serializers import BookSerializer

# List all books
class BookList(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]  # Read-only access for unauthenticated users

    # Add filtering, searching, and ordering backends
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]

    # Configure fields for filtering, searching, and ordering
    filterset_fields = ['title', 'author__name', 'publication_year']  # Filter by title, author's name, and year
    search_fields = ['title', 'author__name']  # Search by title or author's name
    ordering_fields = ['title', 'publication_year']  # Order by title or year
    ordering = ['title']  # Default ordering by title


# Authentication and API Documentation View
@api_view(['GET'])
@permission_classes([AllowAny])
def api_info(request):
    """
    API Information and Authentication Guide
    
    This endpoint provides information about the API and how to authenticate.
    
    Authentication Endpoints:
    - POST /api-token-auth/ - Get authentication token
      Body: {"username": "your_username", "password": "your_password"}
      Returns: {"token": "your_token"}
    
    Book API Endpoints:
    - GET /api/books_all/ - List all books (no auth required)
    - GET /api/books_all/<id>/ - Get specific book (no auth required)
    - POST /api/books_all/ - Create new book (requires auth token)
    - PUT /api/books_all/<id>/ - Update book (requires auth token)
    - DELETE /api/books_all/<id>/ - Delete book (requires auth token)
    
    To use authenticated endpoints:
    1. Get token from /api-token-auth/
    2. Include header: Authorization: Token <your_token>
    """
    return Response({
        'message': 'Book API with Authentication',
        'authentication': {
            'token_endpoint': '/api-token-auth/',
            'method': 'POST',
            'body': {'username': 'your_username', 'password': 'your_password'},
            'response': {'token': 'your_token'}
        },
        'endpoints': {
            'books': {
                'list': 'GET /api/books_all/',
                'detail': 'GET /api/books_all/<id>/',
                'create': 'POST /api/books_all/',
                'update': 'PUT /api/books_all/<id>/',
                'delete': 'DELETE /api/books_all/<id>/'
            }
        },
        'permissions': {
            'read_operations': 'No authentication required',
            'write_operations': 'Authentication token required'
        }
    })
    

# Retrieve a single book by ID
class DetailView(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]  # Read-only access for unauthenticated users

# Add a new book
class CreateView(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]  # Only authenticated users can create

# Update an existing book
class UpdateView(generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]  # Only authenticated users can update

# Delete a book
class DeleteView(generics.DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]  # Only authenticated users can delete

# BookViewSet for all CRUD operations
class BookViewSet(viewsets.ModelViewSet):
    """
    A ViewSet for viewing and editing book instances.
    Provides 'list', 'create', 'retrieve', 'update' and 'destroy' actions.
    
    Authentication & Permissions:
    - GET requests (list, retrieve): Available to all users (read-only)
    - POST, PUT, PATCH, DELETE requests: Require authentication token
    
    To authenticate:
    1. Get token: POST /api-token-auth/ with username and password
    2. Use token: Include 'Authorization: Token <your_token>' in request headers
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]  # Read-only for unauthenticated users, full access for authenticated
    
    # Add filtering, searching, and ordering backends
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    
    # Configure fields for filtering, searching, and ordering
    filterset_fields = ['title', 'author__name', 'publication_year']
    search_fields = ['title', 'author__name']
    ordering_fields = ['title', 'publication_year']
    ordering = ['title']  # Default ordering by title
