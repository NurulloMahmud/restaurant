from django.db import models
from django.core.validators import MinValueValidator



class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Food(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    available_qty = models.IntegerField(default=0, validators=[MinValueValidator(0)])
    category = models.ForeignKey(Category, on_delete=models.CASCADE),
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name

