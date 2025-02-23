from django.db import models


# Author Model
class Author(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


# Book Model (One Author -> Many Books)
class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name="books")

    def __str__(self):
        return self.title


# Library Model (Many Books -> Many Libraries)
class Library(models.Model):
    name = models.CharField(max_length=255)
    books = models.ManyToManyField(Book, related_name="libraries")

    def __str__(self):
        return self.name


# Librarian Model (One Library -> One Librarian)
class Librarian(models.Model):
    name = models.CharField(max_length=255)
    library = models.OneToOneField(
        Library, on_delete=models.CASCADE, related_name="librarian"
    )

    def __str__(self):
        return self.name
