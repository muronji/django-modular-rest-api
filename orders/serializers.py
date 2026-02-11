from rest_framework import serializers
from .models import Order

class OrderSerializer(serializers.ModelSerializer):
    customer_name = serializers.CharField(
    source='customer.__str__',
    read_only=True
)
    
    class Meta:
        model = Order
        fields = '__all__'
