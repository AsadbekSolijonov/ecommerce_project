import django_filters
from backend.apps.products.models import Product


class ProductFilterSet(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='icontains')
    price = django_filters.RangeFilter()
    subcategory = django_filters.CharFilter(field_name='subcategory__name', lookup_expr='icontains')
    category = django_filters.CharFilter(field_name='subcategory__category__name', lookup_expr='icontains')

    class Meta:
        model = Product
        fields = ['name', 'price', 'subcategory', 'category']
