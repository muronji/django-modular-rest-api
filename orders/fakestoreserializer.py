from rest_framework import serializers
from .models import Order, Customer

class ExternalOrderSerializer(serializers.Serializer):
    customer = serializers.IntegerField()
    total_amount = serializers.DecimalField(max_digits=10, decimal_places=2)
    status = serializers.BooleanField(default=False)