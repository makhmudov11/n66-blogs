from django.contrib.auth.models import User
from django.db import models

from apps.products.models import BaseProductModel, Product



class Order(models.Model):
    STATUS_CHOICES = (
        ('pending', 'Pending'),
        ('paid', 'Paid'),
        ('shipped', 'Shipped'),
        ('delivered', 'Delivered'),
        ('canceled', 'Canceled'),
    )
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True, related_name='products')
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='orders'
    )
    total_price = models.DecimalField(
        max_digits=10, decimal_places=2, default=0
    )
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='pending'
    )
    def __str__(self):
        return f"Order {self.id} by {self.user.username}"



