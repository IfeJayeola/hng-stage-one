import django_filters
from .models import PropertyModel


class StringFilter(django_filters.FilterSet):
    is_palindrome = django_filters.BooleanFilter(field_name='is_palindrome')
    min_length = django_filters.NumberFilter(field_name='length', lookup_expr='gte')
    max_length = django_filters.NumberFilter(field_name='length' lookup_expr='lte')
    word_count = django_filters.NumberFilter(field_name='lookup_expr='exact')
    contains_character = django_filters.CharFilter(field_name= 'value', lookup_expr='icontains')


    class Meta:
        model = PropertyModel
        fields = ['is_palindrome', 'length', 'word_count']
