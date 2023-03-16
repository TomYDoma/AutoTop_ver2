from django.contrib import admin

from order.models import Order, Status, TypesWork, Category, Autopart, OrderAutopart

admin.site.register(TypesWork)
admin.site.register(Category)
admin.site.register(Status)

class ItemInline(admin.StackedInline):
    model = OrderAutopart
    extra = 0

class CartAdmin(admin.ModelAdmin):
    inlines = [ItemInline]
    list_display = ["created", "total_price", "paid"]


admin.site.register(Order, CartAdmin)
admin.site.register(Autopart)



