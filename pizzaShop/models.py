from django.db import models

# Create your models here.
class Pizza(models.Model):	
	title = models.CharField(max_length = 100)
	image = models.ImageField(upload_to = 'pizzaShop/images')
	small = models.CharField(max_length = 10)
	medium = models.CharField(max_length = 10)
	large = models.CharField(max_length = 10)
	description = models.TextField()
	
	def __str__(self):
		return self.title
