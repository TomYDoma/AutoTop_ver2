from django.template.defaulttags import url
from django.urls import path, re_path
from django.conf import settings
from django.conf.urls.static import static

from . import views



app_name = 'shop'
urlpatterns = [
    #path('feedback_new', views.createFeedback, name='feedback_new'),
    path('product_list/', views.product_list, name='product_list'),
    re_path(r'^(?P<category_slug>[-\w]+)/$',
        views.product_list,
        name='product_list_by_category'),
    re_path(r'^(?P<id>\d+)/(?P<slug>[-\w]+)/$',
        views.product_detail,
        name='product_detail'),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
