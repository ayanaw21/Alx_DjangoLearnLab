from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from .models import Book, Author
from django.contrib.auth.models import User

class BookTests(APITestCase):
    def setUp(self):
        # Create test data
        self.user = User.objects.create_user(
            username='testuser', 
            password='testpass123'
        )
        self.author = Author.objects.create(name='Test Author')
        self.book = Book.objects.create(
            title='Test Book',
            publication_year=2020,
            author=self.author
        )

    def test_list_books(self):
        url = reverse('book-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)