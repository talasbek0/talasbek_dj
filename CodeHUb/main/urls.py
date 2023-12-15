from django.urls import path
from .views import CategoryAPIView, ProductAPIView, OrderAPIView, ListOrdersAPIView, OrderDetailAPIView

urlpatterns = [
    path('categories/', CategoryAPIView.as_view(), name='category_list'),
    path('products/', ProductAPIView.as_view(), name='category_products'),
    path('order/', OrderAPIView.as_view(), name='order'),
    path('order_list/', ListOrdersAPIView.as_view(), name='order_list'),
    path('order_number/', ListOrdersAPIView.as_view(), name='order_number'),
    path('order_detail/<int:id>/', OrderDetailAPIView.as_view(), name='order_detail')
]
