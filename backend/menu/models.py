from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Food(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    available_qty = models.IntegerField(default=0)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
