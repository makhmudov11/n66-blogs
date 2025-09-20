from decimal import Decimal

from rest_framework import status
from rest_framework.generics import ListCreateAPIView, RetrieveAPIView, ListAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from apps.cart.models import Cart
from apps.cart.permissions import IsOwner
from apps.orders.models import Order, OrderItem
from apps.orders.serializers import OrderSerializer, OrderItemSerializer


class OrderListCreateAPIView(ListCreateAPIView):
    permission_classes = [IsAuthenticated, IsOwner]
    serializer_class = OrderSerializer

    def get_queryset(self):
        return Order.objects.filter(user=self.request.user)

    def list(self, request, *args, **kwargs):
        orders = self.get_queryset()
        serializer = self.serializer_class(orders, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        cart = Cart.objects.filter(user=request.user).first()
        if not cart.cart_items.exists():
            return Response({"message": "Savat bo'sh"}, status=status.HTTP_400_BAD_REQUEST)

        order = Order.objects.create(user=request.user)
        total_price = 0

        for item in cart.cart_items.all():
            print(item.price)
            price = Decimal(item.product.price) * int(item.quantity)
            # print(price)
            OrderItem.objects.create(
                order=order,
                product=item.product,
                quantity=item.quantity,
                price=price
            )
            total_price += price

        order.total_price = total_price
        order.save()

        cart.cart_items.all().delete()

        serializer = self.serializer_class(order)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class OrderItemRetrieveAPIView(RetrieveAPIView):
    serializer_class = OrderItemSerializer
    permission_classes = [IsAuthenticated, IsOwner]
    queryset = OrderItem.objects.all()


class OrderAdminListAPIView(ListAPIView):
    serializer_class = OrderSerializer
    permission_classes = []
    queryset = Order.objects.all()
