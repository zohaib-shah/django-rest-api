from django.db import models
class Category(models.Model):
	title = models.CharField(max_length=200)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	def __str__(self):
		return self.title
class Tag(models.Model):
	title = models.CharField(max_length=200)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	def __str__(self):
		return self.title
class Product(models.Model):
	title = models.CharField(max_length=200)
	description = models.TextField()
	category = models.ForeignKey(Category,on_delete=models.DO_NOTHING)
	price = models.DecimalField(max_digits=10,decimal_places=2)
	tags = models.ManyToManyField(Tag)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	def __str__(self):
		return self.title