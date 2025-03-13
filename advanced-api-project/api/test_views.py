from django.contrib.auth.models import User
from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from .models import Book, Author

class BookAPITestCase(TestCase):
    def setUp(self):
        """
        Set up test environment:
        - Create a test user.
        - Create test books.
        - Initialize API client.
        """
        self.client = APIClient()
        self.author1 = Author.objects.create(name = "Author One")
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.book1 = Book.objects.create(title='News Today', author=self.author1, publication_year=2020)
        self.book2 = Book.objects.create(title='Black Pather', author=self.author1, publication_year=2021)

    def test_list_books(self):
        """Test retrieving all books."""
        response = self.client.get('/api/books/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.json()), 2)

    def test_create_book_authenticated(self):
        """Test creating a new book with authentication."""
        self.client.login(username='testuser', password='testpassword')
        data = {"title": "Madison", "author": self.author1.id, "publication_year": 2022}
        response = self.client.post('/api/books/create/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 3)

    def test_create_book_unauthenticated(self):
        """Test that unauthenticated users cannot create books."""
        data = {"title": "Learn Django", "author": self.author1.id, "publication_year": 2023}
        response = self.client.post('/api/books/create/', data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_get_book_detail(self):
        """Test retrieving a single book by ID."""
        response = self.client.get(f'/api/books/{self.book1.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], 'News Today')

    def test_update_book_authenticated(self):
        """Test updating a book with authentication."""
        self.client.login(username='testuser', password='testpassword')
        data = {"title": "Updated News Today", "author": self.author1.id, "publication_year": 2020}
        response = self.client.put(f'/api/books/update/{self.book1.id}/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book1.refresh_from_db()
        self.assertEqual(self.book1.title, "Updated News Today")

    def test_delete_book_authenticated(self):
        """Test deleting a book with authentication."""
        self.client.login(username='testuser', password='testpassword')
        response = self.client.delete(f'/api/books/delete/{self.book1.id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 1)

    def test_delete_book_unauthenticated(self):
        """Test that unauthenticated users cannot delete books."""
        response = self.client.delete(f'/api/books/delete/{self.book1.id}/')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_search_books(self):
        """Test searching for books by title."""
        response = self.client.get("/api/books/?search=news")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_order_books(self):
        """Test ordering books by publication year."""
        response = self.client.get('/api/books/?ordering=publication_year')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        books = response.json()
        self.assertTrue(books[0]['publication_year'] <= books[1]['publication_year'])
        self.assertTrue(len(response.data), 3)
