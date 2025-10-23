from django.shortcuts import render
from rest_framework import viewsets,permissions
from .models import Product, Order
from .permissions import IsAdminOrReadOnly
from .serializers import ProductSerializer, OrderSerializer
# Create your views here.
class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAdminOrReadOnly]
    
class OrderViewSet(viewsets.ModelViewSet):
    serializer_class = OrderSerializer
    permission_classes = [IsAdminOrReadOnly]
    def get_queryset(self):
        user = self.request.user
        if user.is_staff:
            return Order.objects.all()
        return Order.objects.filter(user=user)
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)