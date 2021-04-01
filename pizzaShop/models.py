from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Pizza(models.Model):	
	title = models.CharField(max_length = 100)
	image = models.ImageField(upload_to = 'pizzaShop/images')
	small = models.CharField(max_length = 10)
	medium = models.CharField(max_length = 10)
	large = models.CharField(max_length = 10)
	description = models.TextField()
	user = models.ForeignKey(User, on_delete = models.CASCADE)
	
	def __str__(self):
		return self.title
