from rest_framework import serializers

from apps.accounts.serializers import UserSerializer
from apps.orders.models import Order
from apps.products.serializers import ProductSerializer


class OrderSerializer(serializers.ModelSerializer):
    user = UserSerializer
    product = ProductSerializer
    class Meta:
        model = Order
        fields = ['id', 'user', 'product', 'created_at', 'quantity', 'total_price', 'status']

