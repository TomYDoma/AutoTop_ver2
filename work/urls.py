from django.template.defaulttags import url
from django.urls import path, re_path
from django.conf import settings
from django.conf.urls.static import static
from . import views

app_name = 'work'
urlpatterns = [
    path('work_list/', views.work_list, name='work_list'),
    re_path(r'^(?P<category_slug>[-\w]+)/$', views.work_list, name='work_list_by_category'),
    re_path(r'^(?P<id>\d+)/(?P<slug>[-\w]+)/$', views.work_detail, name='work_detail'),


] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
