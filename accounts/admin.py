from django.contrib import admin
from .models import Profile, Car, Order, CompositionWorks, Status

admin.site.register(Profile)
admin.site.register(Car)
admin.site.register(Order)
admin.site.register(CompositionWorks)
admin.site.register(Status)
