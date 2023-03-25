from django.contrib import admin
from .models import Profile, Car, TypeCar

admin.site.register(Profile)
admin.site.register(Car)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(TypeCar, CategoryAdmin)