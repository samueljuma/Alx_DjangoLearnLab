from rest_framework.pagination import PageNumberPagination


class StandardResultsSetPagination(PageNumberPagination):
    page_size = 10  # Number of items per page
    page_size_query_param = "page_size"  # Allow clients to set page size
    max_page_size = 100  # Maximum allowed page size
