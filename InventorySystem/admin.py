from django.contrib import admin

from InventorySystem.models import Customer, Product, Order


class OrderInfo(admin.TabularInline):
    model = Order
    extra = 2


class CustomerAdmin(admin.ModelAdmin):
    inlines = [OrderInfo]
    list_display = ['pk', 'customerID', 'Company', 'ContactName',
                    'Address', 'PostCode', 'PhoneNumber']
    list_filter = ['customerID']
    search_fields = ['Company']
    list_per_page = 5
    actions_on_top = False
    actions_on_bottom = True


class ProductAdmin(admin.ModelAdmin):
    list_display = ['pk', 'ProduceID', 'ProductName', 'ProductDetail']
    list_filter = ['ProduceID']
    search_fields = ['ProductName']
    list_per_page = 5
    actions_on_top = False
    actions_on_bottom = True


class OrderAdmin(admin.ModelAdmin):
    list_display = ['pk', 'OrderID', 'OrderNumber', 'CustomerID', 'OrderQTY', 'OrderDate']
    list_filter = ['OrderID']
    search_fields = ['OrderID']
    list_per_page = 5
    actions_on_top = False
    actions_on_bottom = True


admin.site.register(Customer, CustomerAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Order, OrderAdmin)