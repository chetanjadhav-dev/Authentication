from django.urls import path,include
from . import views

urlpatterns = [
    path('login/', views.login, name='login'),
    path('signup/', views.signup, name='signup'),
    path('logout/', views.logout, name='logout'),
    path('test_token/', views.test_token, name='test_token'),
    path('', include('orders.urls')),
    path('', include('payments.urls')),
    path('', include('notifications.urls')),
]
