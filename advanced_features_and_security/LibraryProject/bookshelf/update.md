# Update Book

## Command

```python
from bookshelf.models import Book

book.title = "Nineteen Eighty-Four"
book.save()
print(Book.objects.get(id=book.id))


```

## Output

```
Nineteen Eighty-Four by George Orwell (1949)
```
