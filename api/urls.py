from django.contrib import admin
from django.urls import path
from rest_framework import routers
from app.views import CategoryViewSet
from app.views import TagViewSet
from app.views import ProductViewSet

r = routers.SimpleRouter()
r.register(r'categories',CategoryViewSet)
r.register(r'tags',TagViewSet)
r.register(r'products',ProductViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
]

urlpatterns += r.urls
