from rest_framework import serializers
from .models import Book, Author
import datetime


class BookSerialiser(serializers.ModelSerializer):
    """Serializer for the Book model."""

    class Meta:
        model = Book
        fields = ["id", "title", "publication_year", "author"]

    def validate_publication_year(self, value):
        """Ensure the publication year is not in the future."""
        current_year = datetime.date.today().year
        if value > current_year:
            raise serializers.ValidationError(
                "Publication year cannot be in the future."
            )
        return value


class AuthorSerializer(serializers.ModelSerializer):
    """Serializer for the Author model including nested books."""

    books = BookSerialiser(many=True, read_only=True)

    class Meta:
        model = Author
        fields = ["id", "name", "books"]
