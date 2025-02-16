# CRUD OPERATIONS

## Create a Book Instance

### Command

```python
from bookshelf.models import Book

# Creating a new book instance
book = Book.objects.create(
    title="1984",
    author="George Orwell",
    publication_year=1949
)

# Display the created book
print(book)
```

### Output

```
1984 by George Orwell (1949)
```

## Retrieve Book

### Command

```python
from bookshelf.models import Book

book = Book.objects.get(title="1984")
print(book.title, book.author, book.publication_year)

```

### Output

```
1984 George Orwell 1949
```

## Update Book

### Command

```python
from bookshelf.models import Book

book.title = "Nineteen Eighty-Four"
book.save()
print(Book.objects.get(id=book.id))


```

### Output

```
Nineteen Eighty-Four by George Orwell (1949)
```

## Delete Book

### Command

```python
from bookshelf.models import Book

book.delete()
print(Book.objects.all())

```

### Output

```
<QuerySet []>
```
