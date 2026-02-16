from django.urls import path
from .views import OrderDetailView, OrderListCreateView, FetchExternalOrdersView

urlpatterns = [
    path('orders/', OrderListCreateView.as_view(), name='order-list-create'),
    path('orders/<int:pk>/', OrderDetailView.as_view(), name='order-detail'),
     path('external-orders/', FetchExternalOrdersView.as_view(), name='fetch-external-orders'),
]
