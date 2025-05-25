from django.urls import path
from django_filters.views import FilterView
from rest_framework.routers import DefaultRouter

from backend.apps.products.filters import ProductFilterSet
from backend.apps.products.models import Product
from backend.apps.products.views import (CategoryViewSet,
                                         SubCategoryViewSet,
                                         ProductViewSet)

routers = DefaultRouter()
routers.register('category', CategoryViewSet)
routers.register('subcategory', SubCategoryViewSet)
routers.register('products', ProductViewSet)

urlpatterns = []
urlpatterns += routers.urls
