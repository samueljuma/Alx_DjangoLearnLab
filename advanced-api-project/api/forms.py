from django import forms
from datetime import date
from .models import Book

class BookAdminForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = "__all__"

    def clean_publication_year(self):
        """Ensure publication year is not in the future."""
        publication_year = self.cleaned_data.get("publication_year")
        current_year = date.today().year
        if publication_year > current_year:
            raise forms.ValidationError("Publication year cannot be in the future.")
        return publication_year
