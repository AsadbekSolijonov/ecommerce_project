from rest_framework import serializers

from backend.apps.products.models import SubCategory
from backend.apps.products.serializers.product import ProductSerializer


class SubCategorySerializer(serializers.ModelSerializer):
    products = ProductSerializer(many=True, read_only=True)

    class Meta:
        model = SubCategory
        fields = ['id', 'name', 'category', 'products']
        read_only_fields = ('id', )
