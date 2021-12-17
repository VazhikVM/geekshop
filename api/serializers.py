from rest_framework import serializers
from mainapp.models import Product, ProductCategory


class ProductSerializers(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class CategorySerializers(serializers.ModelSerializer):
    class Meta:
        model = ProductCategory
        fields = '__all__'

