from django.urls import path
from .views import UserCartListCreateAPIView, UserItemRetrieveUpdateDestroyAPIView

app_name = 'cart'

urlpatterns = [
    path('', UserCartListCreateAPIView.as_view(), name='list'),
    path('items/<int:pk>/', UserItemRetrieveUpdateDestroyAPIView.as_view(), name='item_detail')
]