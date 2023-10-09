from django.contrib.auth.models import User

from rest_framework import serializers

from shop.models import Category, Product

class CategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Category
        fields = ["slug", "name"]

class ProductSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:

        model = Product
        fields = ["category", "slug", "name", "description", "price"]