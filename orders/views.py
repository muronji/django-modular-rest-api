from rest_framework.views import APIView

from orders.services import fetch_and_save_external_orders
from .models import Order
from .serializers import OrderSerializer
from rest_framework.response import Response
from rest_framework import status
from common.permissions import IsStaffOrReadOnly

class OrderListCreateView(APIView):
    permission_classes = [IsStaffOrReadOnly]

    def get(self, request):
        orders = Order.objects.select_related('customer').order_by('-created_at')
        serializer = OrderSerializer(orders, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = OrderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        print(serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class OrderDetailView(APIView):
    permission_classes = [IsStaffOrReadOnly]
    def get_object(self, pk):
        try:
            return Order.objects.get(pk=pk)
        except Order.DoesNotExist:
            return None
        
    def get(self, request, pk):
        order = self.get_object(pk)
        if order is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = OrderSerializer(order)
        return Response(serializer.data)
    
    def put(self, request, pk):
        order = self.get_object(pk)
        if order is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = OrderSerializer(order, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def patch(self, request, pk):
        order = self.get_object(pk)
        if order is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = OrderSerializer(order, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        order = self.get_object(pk)
        if order is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        order.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
   
class FetchExternalOrdersView(APIView):
    permission_classes = [IsStaffOrReadOnly]
    def get(self, request):
        orders, error = fetch_and_save_external_orders()
        if error:
            return Response({"error": error}, status=status.HTTP_503_SERVICE_UNAVAILABLE)

        serializer = OrderSerializer(orders, many=True)
        return Response(serializer.data, status=status.HTTP_201_CREATED)