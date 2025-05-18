from rest_framework import serializers

from backend.apps.products.models import Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'price', 'description', 'stock', 'subcategory', 'image', 'created_at', 'updated_at']
        read_only_fields = ('id', 'created_at', 'updated_at')
