from django.contrib import admin

from .models import Author, Book, Library, Librarian


class BookAdmin(admin.ModelAdmin):
    list_display = ("title", "author")
    list_filter = ("author",)
    search_fields = ("title", "author__name")


class AuthorAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)

class LibraryAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)


admin.site.register(Book, BookAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Library, LibraryAdmin)
