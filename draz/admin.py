from django.contrib import admin

# Register your models here.
from .models import Product,Order, OrderItem
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = 'name','image','description','created_at',
    search_fields = 'name','description',
    
class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 0
    
@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = 'id','user','created_at','total_price',
    search_fields = 'user__username','id',
    list_filter = 'created_at','user',
    inlines = [OrderItemInline]
    
@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = 'order','product','quantity',
    search_fields = 'order','product',