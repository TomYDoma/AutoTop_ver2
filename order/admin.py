from django.contrib import admin

from order.models import Order, Status, TypesWork, Category, CompositionOrder, Autopart

admin.site.register(TypesWork)
admin.site.register(Order)
admin.site.register(Category)
admin.site.register(Autopart)
admin.site.register(CompositionOrder)
admin.site.register(Status)
