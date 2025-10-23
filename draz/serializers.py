from rest_framework import serializers
from .models import Product, Order,OrderItem



class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
        
class OrderItemSerializer(serializers.ModelSerializer):
    product_name = serializers.ReadOnlyField(source='product.name')
    product_price = serializers.ReadOnlyField(source='product.price')
    
    class Meta:
        model = OrderItem
        fields = ['product', 'product_name', 'product_price', 'quantity']
        
class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True)
    
    class Meta:
        model = Order
        fields = '__all__'
        read_only_fields = ['user', 'created_at', 'total_price']
    def create(self, validated_data):
        items_data = validated_data.pop('items', [])
        validated_data.pop('user', None)
        user = self.context['request'].user
        order = Order.objects.create(user=user, **validated_data)
        total = 0
        for item in items_data:
            product = item['product']
            quantity = item['quantity']
            subtotal = product.price * quantity
            total += subtotal
            OrderItem.objects.create(order=order, product=product, quantity=quantity)
        order.total_price = total
        order.save()
        return order
                