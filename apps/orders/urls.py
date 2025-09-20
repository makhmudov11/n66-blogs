from django.urls import path

from apps.orders.views import OrderListCreateAPIView, OrderItemRetrieveAPIView, OrderAdminListAPIView

app_name = 'orders'
urlpatterns = [
    path('', OrderListCreateAPIView.as_view(), name='list'),
    path('<int:pk>/', OrderItemRetrieveAPIView.as_view(), name='detail'),
    path('admin/', OrderAdminListAPIView.as_view(), name='admin_list'),
]