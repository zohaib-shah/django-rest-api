from django.contrib import admin
from .models import Category
from .models import Product
from .models import Tag

admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Tag)
