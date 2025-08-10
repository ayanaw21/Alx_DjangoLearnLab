from django.urls import path
from .views import ListView, DetailView, CreateView, UpdateView, DeleteView

urlpatterns = [
    # List all books
    path('books/', ListView.as_view(), name='book-list'),
    
    # Get single book details
    path('books/<int:pk>/', DetailView.as_view(), name='book-detail'),
    
    # Create new book
    path('books/create/', CreateView.as_view(), name='book-create'),
    
    # Update existing book - Changed to match requirement
    path('books/update/<int:pk>/', UpdateView.as_view(), name='book-update'),
    
    # Delete book - Changed to match requirement
    path('books/delete/<int:pk>/', DeleteView.as_view(), name='book-delete'),
]