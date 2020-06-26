import django_filters
from .models import Book


class BookFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(field_name="name_book", lookup_expr='iexact')

    class Meta:
        model = Book
        fields = ['name_book', 'author_id', 'category_id', 'publishingYear']

