from django.contrib.auth.models import User

from rest_framework import viewsets
#from rest_framework import permissions

from .serializers import CategorySerializer, ProductSerializer
from shop.models import Category, Product


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer