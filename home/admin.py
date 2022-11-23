from django.contrib import admin
from .models import SpecialistAdmin, SpecialistList, mainCart, FeedbackList


admin.site.register(SpecialistAdmin)
admin.site.register(SpecialistList)
admin.site.register(mainCart)
admin.site.register(FeedbackList)
