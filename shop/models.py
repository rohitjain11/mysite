from django.db import models

class User(models.Model):
    name =models.CharField(max_length=64)
    username = models.CharField(max_length=64)
    num = models.CharField(max_length=64)
    pword = models.CharField(max_length=64)
    email = models.EmailField()

class Product(models.Model):
    p_name =models.CharField(max_length=64)
    quantity = models.CharField(max_length=64)
    image = models.ImageField(upload_to='images/')