from django.urls import path
from . import views

urlpatterns = [
    path('books/', ListView.as_view(), name='book-list'),
    
    # Get single book details
    path('books/<int:pk>/', DetailView.as_view(), name='book-detail'),
    
    # Create new book
    path('books/create/', CreateView.as_view(), name='book-create'),
    
    # Update existing book
    path('books/<int:pk>/update/', UpdateView.as_view(), name='book-update'),
    
    # Delete book
    path('books/<int:pk>/delete/', DeleteView.as_view(), name='book-delete'),
]