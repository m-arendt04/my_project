from django.db import models


# Create your models here.
class ProductCategory(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):
        return 'Kategoria: ' + self.name


class Product(models.Model):
    name = models.CharField(max_length=128)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    usage_per_unit = models.DecimalField(max_digits=5, decimal_places=2)
    capacity = models.DecimalField(max_digits=5, decimal_places=2)
    product_category = models.ForeignKey(ProductCategory, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.name
