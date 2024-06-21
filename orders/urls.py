from django.urls import path
from . import views

urlpatterns = [
    path('orders/', views.OrderListCreateAPIView.as_view(), name='order-list-create'),
    path('orders/<int:pk>/', views.OrderDetailAPIView.as_view(), name='order-detail'),
    path('orders/create/', views.create_order, name='create-order'),  # Add this if using function-based view
]
