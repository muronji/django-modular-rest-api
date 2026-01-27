from rest_framework.viewsets import ModelViewSet
from .models import Order
from .serializers import OrderSerializer
from common.permissions import IsStaffOrReadOnly

class OrderViewSet(ModelViewSet):
    queryset = Order.objects.select_related('customer').order_by('-created_at')
    serializer_class = OrderSerializer
    permission_classes = [IsStaffOrReadOnly]

