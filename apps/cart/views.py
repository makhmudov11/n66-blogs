from statistics import quantiles

from django.shortcuts import render
from rest_framework import status
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from apps.cart.models import CartItem, Cart
from apps.cart.permissions import IsOwner
from apps.cart.serializers import CartItemSerializer
from apps.products.models import Product


class UserCartListCreateAPIView(ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = CartItemSerializer

    def get_queryset(self):
        return CartItem.objects.filter(cart__user=self.request.user)

    def list(self, request, *args, pk=None, **kwargs, ):
        cart_items = self.get_queryset()
        if not cart_items:
            return Response(data={"message": "Savat bo'sh"}, status=status.HTTP_404_NOT_FOUND)
        serializer = self.serializer_class(cart_items, many=True)
        return Response(
            data=serializer.data,
            status=status.HTTP_200_OK
        )

    def post(self, request, *args, **kwargs):
        user_cart, _ = Cart.objects.get_or_create(user=request.user)
        product_id = request.data.get("product_id")
        quantity = request.data.get("quantity", 1)

        try:
            product = Product.objects.get(id=product_id)
        except Product.DoesNotExist:
            return Response({"message": "Product topilmadi"}, status=status.HTTP_404_NOT_FOUND)

        if quantity <= product.quantity:
            product.quantity -= quantity
            product.save()
            cart_item, created = CartItem.objects.get_or_create(cart=user_cart, product=product)
            cart_item.quantity = cart_item.quantity + int(quantity) if not created else int(quantity)
            cart_item.price = product.price
            print(product.price)
            print(cart_item)
            cart_item.save()

            serializer = self.serializer_class(cart_item)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(
                {"message": f"Mahsulot soni {quantity} dan kam, qolgan mahsulot soni: {product.quantity}"},
                status=status.HTTP_404_NOT_FOUND)


class UserItemRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated, IsOwner]
    serializer_class = CartItemSerializer

    def get_queryset(self):
        return CartItem.objects.filter(cart__user=self.request.user)

    def patch(self, request, *args, **kwargs):
        cart_item = self.get_object()
        quantity = self.request.data.get('quantity')

        if quantity is not None:
            cart_item.quantity = int(quantity)
            cart_item.save()
        serializer = self.serializer_class(cart_item)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.delete()
        return Response(data={"message": "Mahsulot ochirildi"}, status=status.HTTP_200_OK)
