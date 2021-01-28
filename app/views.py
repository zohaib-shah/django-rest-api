from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import Category
from .models import Tag
from .models import Product
from .serializers import CategorySerializer
from .serializers import TagSerializer
from .serializers import ProductSerializer
# Create your views here.
class CategoryViewSet(ModelViewSet):
	model = Category
	serializer_class = CategorySerializer
	queryset = Category.objects.all()
class TagViewSet(ModelViewSet):
	model = Tag
	serializer_class = TagSerializer
	queryset = Tag.objects.all()
class ProductViewSet(ModelViewSet):
	model = Product
	serializer_class = ProductSerializer
	queryset = Product.objects.all()