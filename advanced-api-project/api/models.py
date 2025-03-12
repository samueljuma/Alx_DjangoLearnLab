from django.db import models


class Author(models.Model):
    """Model representing a book."""

    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Book(models.Model):
    """Model representing a book."""

    title = models.CharField(max_length=100)
    publication_year = models.IntegerField(null=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name="books")

    def __str__(self):
        return self.title
