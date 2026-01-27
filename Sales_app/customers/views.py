from rest_framework.viewsets import ModelViewSet
from .models import Customer
from .serializers import CustomerSerializer
from common.permissions import IsStaffOrReadOnly

class CustomerViewSet(ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    permission_classes = [IsStaffOrReadOnly]

