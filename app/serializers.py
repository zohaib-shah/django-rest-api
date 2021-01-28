from rest_framework import serializers
from .models import Category
from .models import Tag
from .models import Product
class CategorySerializer(serializers.ModelSerializer):
	class Meta:
		model = Category
		fields = ('title',)
class TagSerializer(serializers.ModelSerializer):
	class Meta:
		model = Tag
		fields = ('title',)
class ProductSerializer(serializers.ModelSerializer):
	class Meta:
		model = Product
		fields = ('title','description','category','price','tags',)
	def to_representation(self, obj):
		data = super().to_representation(obj)
		#data is of type orderedDict
		#orderedDict is similar to Dict data type with an exception of preserving order
		#we can customize data from this point as per our needs
		tags_info = Tag.objects.filter(pk__in=data['tags'])
		cat_name = Category.objects.get(pk=data['category'])
		new_tags_fields = []
		for ti in tags_info:
			new_tags_fields.append(ti.title)
		data['tags'] = new_tags_fields
		data['category'] = cat_name.title
		#once done we have to return the data variable (orderedDict)
		return data