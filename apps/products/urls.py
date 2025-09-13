from django.urls import path

from apps.products.views import ProductListCreateAPIView, ProductRetrieveUpdateDestroyAPIView, \
    CategoryListCreateAPIView, CategoryRetrieveUpdateDestroyAPIView

app_name = 'products'

urlpatterns = [
    path('', ProductListCreateAPIView.as_view(), name='list'),
    path('<int:pk>/', ProductRetrieveUpdateDestroyAPIView.as_view(), name='detail'),
    path('category/', CategoryListCreateAPIView.as_view(), name='category'),
    path('category/<int:pk>/', CategoryRetrieveUpdateDestroyAPIView.as_view(), name='category_detail'),
]