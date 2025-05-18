from django.urls import path
from rest_framework.routers import DefaultRouter

from backend.apps.products.views import (CategoryViewSet,
                                         SubCategoryViewSet,
                                         ProductViewSet)

routers = DefaultRouter()
routers.register('category', CategoryViewSet)
routers.register('subcategory', SubCategoryViewSet)
routers.register('products', ProductViewSet)

urlpatterns = []
urlpatterns += routers.urls
