from django.urls import path

from apps.orders.views import UserOrderListCreateAPIView, UserOrderDetailAPIView

app_name = 'orders'
urlpatterns = [
    path('', UserOrderListCreateAPIView.as_view(), name='list'),
    path('<int:pk>/', UserOrderDetailAPIView.as_view(), name='detail'),
    path('admin/', UserOrderListCreateAPIView.as_view(), name='list'),
]