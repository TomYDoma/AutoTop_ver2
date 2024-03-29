from django.template.defaulttags import url
from django.urls import path, re_path
from django.conf import settings
from django.conf.urls.static import static
from . import views

app_name = 'cart'
urlpatterns = [
    re_path(r'^$', views.cart_detail, name='cart_detail'),
    re_path(r'^add/(?P<product_id>\d+)/$', views.cart_add, name='cart_add'),
    re_path(r'^remove/(?P<product_id>\d+)/$', views.cart_remove, name='cart_remove'),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

