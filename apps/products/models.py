from django.contrib.auth.models import User
from django.db import models

class BaseProductModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    class Meta:
        abstract = True


class Category(BaseProductModel):
    name = models.CharField(max_length=66, unique=True, verbose_name='name')
    description = models.TextField(blank=True)

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name

class Product(BaseProductModel):
    name = models.CharField(max_length=50)
    quantity = models.PositiveSmallIntegerField()
    description = models.TextField()
    image = models.URLField(default=None, null=True, blank=True)
    price = models.DecimalField(max_digits=15, decimal_places=2, default=0)
    category = models.ForeignKey(Category, related_name='products', on_delete=models.SET_NULL, null=True)
    owner = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='products')
