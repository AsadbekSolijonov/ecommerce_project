from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.viewsets import ModelViewSet

from backend.apps.products.filters import ProductFilterSet
from backend.apps.products.models import (Category,
                                          SubCategory,
                                          Product)

from backend.apps.products.serializers.category import CategorySerializer
from backend.apps.products.serializers.subcategory import SubCategorySerializer
from backend.apps.products.serializers.product import ProductSerializer


# Create your views here.
class CategoryViewSet(ModelViewSet):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()


class SubCategoryViewSet(ModelViewSet):
    serializer_class = SubCategorySerializer
    queryset = SubCategory.objects.all()


class ProductViewSet(ModelViewSet):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_class = ProductFilterSet
