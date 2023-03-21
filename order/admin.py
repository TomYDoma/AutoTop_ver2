from django.contrib import admin
import nested_admin
from order.models import Order, Status,  OrderItem, OrderWork


class ItemInline(nested_admin.NestedTabularInline):
    model = OrderItem
    extra =0

class WorkInline(nested_admin.NestedTabularInline):
    model = OrderWork
    extra =0

class ContestantInline(nested_admin.NestedModelAdmin):
    model = Order
    inlines = [ItemInline, WorkInline,]
    extra = 0


admin.site.register(Order, ContestantInline)

admin.site.register(Status)

