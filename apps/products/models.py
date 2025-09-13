from django.contrib.auth.models import User
from django.db import models

class BaseProductModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    class Meta:
        abstract = True


class Category(BaseProductModel):
    name = models.CharField(max_length=66, unique=True)
    description = models.TextField(blank=True)

class Product(BaseProductModel):
    name = models.CharField(max_length=50)
    quantity = models.PositiveSmallIntegerField()
    description = models.TextField()
    category = models.ForeignKey(Category, related_name='products', on_delete=models.SET_NULL, null=True)
    owner = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='products')
