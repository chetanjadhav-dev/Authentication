from django.urls import path
from . import views

urlpatterns = [
    path('payments/', views.PaymentListCreateAPIView.as_view(), name='payment-list-create'),
    path('payments/<int:pk>/', views.PaymentDetailAPIView.as_view(), name='payment-detail'),
]
