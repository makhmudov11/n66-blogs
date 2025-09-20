from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.response import Response

from apps.blogs.utils.custom_pagination import CustomPageNumberPagination
from apps.products.models import Product
from apps.products.permissions import ProductPermission, ProductDetailPermission, CategoryDetailPermission, \
    CategoryPermission
from apps.products.serializers import ProductSerializer, CategorySerializer


class ProductListCreateAPIView(ListCreateAPIView):
    queryset = Product.objects.all()
    permission_classes = [ProductPermission]
    serializer_class = ProductSerializer
    pagination_class = CustomPageNumberPagination

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            paginated_data = self.get_paginated_response(serializer.data)

            return Response(
                data=paginated_data
            )

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class ProductRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [ProductDetailPermission]


class CategoryListCreateAPIView(ListCreateAPIView):
    queryset = Product.objects.all()
    permission_classes = [CategoryPermission]
    serializer_class = CategorySerializer


class CategoryRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [CategoryDetailPermission]
