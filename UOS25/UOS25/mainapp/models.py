from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=50)
    content = models.CharField(max_length=50)
    
class User(models.Model):
    userId = models.CharField(max_length=50)