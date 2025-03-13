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
- ✅ Installed `django-filters`.
- ✅ Updated `settings.py` to include `'django_filters'`.
- ✅ Enabled filtering in `BookListView` using `DjangoFilterBackend`.
- ✅ Users can now filter books by **title, author name, and publication year** using query parameters.

---

# Search and Ordering Functionality

## Overview
This API provides search and ordering functionality for retrieving book records. Users can filter books by title or author name, and order them based on title or publication year.

## Features
- **Search**: Users can search for books by `title` or `author name`.
- **Ordering**: Users can order results by `title` or `publication year`, in ascending or descending order.
- **Default Ordering**: Results are sorted by `title` by default.

## Configuration in `views.py`
To enable search and ordering, the following configurations are added to `BookListView`:

```python
from rest_framework import generics
from rest_framework.filters import SearchFilter, OrderingFilter
from .models import Book
from .serializers import BookSerializer

class BookListView(generics.ListAPIView):
    """
    API view to retrieve a list of books with search and ordering functionality.
    Users can search by title or author name and order results by title or publication year.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    
    # Enable search and ordering functionality
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ["title", "author__name"]  # Search by title and author name
    ordering_fields = ["title", "publication_year"]  # Order by title and publication year
    ordering = ["title"]  # Default ordering by title
```

## How to Use
### 1️⃣ Searching
Users can search for books by `title` or `author name` using the `search` query parameter.

**Example: Search by title**
```
http://localhost:8000/books/?search=harry
```

**Example: Search by author name**
```
http://localhost:8000/books/?search=rowling
```

### 2️⃣ Ordering
Users can order results by `title` or `publication year` using the `ordering` query parameter.

**Example: Order by title (ascending)**
```
http://localhost:8000/books/?ordering=title
```

**Example: Order by publication year (ascending)**
```
http://localhost:8000/books/?ordering=publication_year
```

**Example: Order by publication year (descending)**
```
http://localhost:8000/books/?ordering=-publication_year
```

💡 **Note:** Prefixing a field with `-` reverses the order (descending).

## Summary
- **Search books** by `title` or `author name` using `?search=your_query`.
- **Sort results** using `?ordering=title` or `?ordering=publication_year`.
- **Reverse sorting** by adding a `-` before the field, e.g., `?ordering=-title`.


