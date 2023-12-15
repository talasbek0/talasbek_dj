from .models import *
from rest_framework import serializers


class CatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('title', 'image')


class ProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = '__all__'


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'


class OrderDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'
