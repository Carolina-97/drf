from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=50)
    images = models.ImageField()
    desc = models.CharField(max_length=300)
    category = models.ForeignKey("Category",on_delete=models.CASCADE)
    price = models.FloatField(max_length=250)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class User(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=12)
    address = models.CharField(max_length=30)


    def __str__(self):
        return self.username