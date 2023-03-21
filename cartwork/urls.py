from django.template.defaulttags import url
from django.urls import path, re_path
from django.conf import settings
from django.conf.urls.static import static
from . import views

app_name = 'cartwork'
urlpatterns = [
    re_path(r'^$', views.cartwork_detail, name='cartwork_detail'),
    re_path(r'^add/(?P<product_id>\d+)/$', views.cartwork_add, name='cartwork_add'),
    re_path(r'^remove/(?P<product_id>\d+)/$', views.cartwork_remove, name='cartwork_remove'),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

