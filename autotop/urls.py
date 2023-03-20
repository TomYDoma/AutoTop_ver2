from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/', include('accounts.urls')),
    path('order/', include('order.urls')),
    path('shop/', include('shop.urls')),
    path('cart/', include('cart.urls')),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)