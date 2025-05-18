from rest_framework import serializers

from backend.apps.products.models import Category
from backend.apps.products.serializers.subcategory import SubCategorySerializer


class CategorySerializer(serializers.ModelSerializer):
    subcategories = SubCategorySerializer(many=True, read_only=True)

    class Meta:
        model = Category
        fields = ['id', 'name', 'subcategories', ]
        read_only_fields = ('id', )
