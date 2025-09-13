from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from apps.products.models import Product
from apps.products.permissions import ProductPermission, ProductDetailPermission, CategoryDetailPermission, \
    CategoryPermission
from apps.products.serializers import ProductSerializer, CategorySerializer


class ProductListCreateAPIView(ListCreateAPIView):
    queryset = Product.objects.all()
    permission_classes = [ProductPermission]
    serializer_class = ProductSerializer

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
