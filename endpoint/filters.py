import django_filters
from .models import StringModel

class StringFilter(django_filters.FilterSet):
    is_palindrome = django_filters.BooleanFilter(field_name='property__is_palindrome')
    min_length = django_filters.NumberFilter(field_name='property__length', lookup_expr='gte')
    max_length = django_filters.NumberFilter(field_name='property__length', lookup_expr='lte')

    class Meta:
        model = StringModel
        fields = ['is_palindrome']
