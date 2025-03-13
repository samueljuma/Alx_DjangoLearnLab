# Book API - Django REST Framework

This API provides endpoints for managing books, including listing, creating, retrieving, updating, and deleting book records.

## Endpoints & Views

### 1. List All Books
**URL:** `GET /books/`  
**View:** `BookListView`  
**Description:**
- Retrieves a list of all books in the database.
- Accessible to all users (unauthenticated users can only read).
- Uses `ListAPIView`.
- Implements `IsAuthenticatedOrReadOnly` permission.

### 2. Create a Book
**URL:** `POST /books/create/`  
**View:** `BookCreateView`  
**Description:**
- Allows authenticated users to create a new book entry.
- Uses `CreateAPIView`.
- Implements `IsAuthenticated` permission to restrict book creation to logged-in users.

### 3. Retrieve a Book by ID
**URL:** `GET /books/<int:pk>/`  
**View:** `BookDetailView`  
**Description:**
- Fetches details of a single book based on its primary key (ID).
- Accessible to all users (unauthenticated users can only read).
- Uses `RetrieveAPIView`.
- Implements `IsAuthenticatedOrReadOnly` permission.

### 4. Update a Book
**URL:** `PUT /books/update/`  
**View:** `BookUpdateView`  
**Description:**
- Updates an existing book's details.
- Only accessible to authenticated users.
- Uses `UpdateAPIView`.
- Implements `IsAuthenticated` permission.

### 5. Delete a Book
**URL:** `DELETE /books/delete/`  
**View:** `BookDeleteView`  
**Description:**
- Deletes a book entry from the database.
- Only accessible to authenticated users.
- Uses `DestroyAPIView`.
- Implements `IsAuthenticated` permission.

## Permissions Used
- `IsAuthenticatedOrReadOnly`: Allows unauthenticated users to read but restricts modifications to authenticated users.
- `IsAuthenticated`: Ensures only logged-in users can create, update, or delete books.

## Installation & Setup
1. Clone the repository:
   ```sh
   git clone <repository-url>
   cd advanced_api_project
   ```
2. Apply migrations:
   ```sh
   python manage.py migrate
   ```
3. Start the development server:
   ```sh
   python manage.py runserver
   ```
4. Access the API at `http://127.0.0.1:8000/`


# Filtering Books in Django REST Framework

This guide explains how to implement filtering for the **Book** model in a Django REST Framework (DRF) project using `django-filters`.

---

## 1️⃣ Install `django-filters`
To enable filtering in DRF, first install the `django-filter` package:
```bash
pip install django-filter
```

Then, add `'django_filters'` to `INSTALLED_APPS` in your `settings.py`:
```python
INSTALLED_APPS = [
    # Other installed apps...
    'django_filters',
]
```

---

## 2️⃣ Update the `BookListView`
Modify your `views.py` to integrate filtering in the **BookListView**:

```python
from django_filters.rest_framework import DjangoFilterBackend  # Import DjangoFilterBackend
from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import Book
from .serializers import BookSerializer

class BookListView(generics.ListAPIView):
    """
    View to list all books with filtering support.
    - Users can filter by `title`, `author__name`, and `publication_year`.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    
    # Enable filtering
    filter_backends = [DjangoFilterBackend]  
    filterset_fields = ['title', 'author__name', 'publication_year']
```

---

## 3️⃣ How to Use Filtering
Users can apply filters using query parameters when making a GET request to the books endpoint:

### 🔹 Example Requests
```bash
GET books/?title=The Great Gatsby
GET books/?author__name=J.K. Rowling
GET books/?publication_year=2020
```

---

## 4️⃣ Summary
✅ Installed `django-filters`.
✅ Updated `settings.py` to include `'django_filters'`.
✅ Enabled filtering in `BookListView` using `DjangoFilterBackend`.
✅ Users can now filter books by **title, author name, and publication year** using query parameters.

---

