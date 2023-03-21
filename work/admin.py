from django.contrib import admin

from shop.admin import CategoryAdmin
from work.models import CategoryWork, Work


class CategoryWorkAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(CategoryWork, CategoryAdmin)


class WorkAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'price']
    list_editable = ['price']
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Work, WorkAdmin)
