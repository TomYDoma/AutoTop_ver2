from django.urls import path, re_path
from django.conf import settings
from django.conf.urls.static import static
from . import views
from .views import BlogListView

urlpatterns = [
    path('', views.index, name = "home"),
    path('contact', views.contact, name = "contact"),
    path('services', views.services, name="services"),
    path('team_specialist', views.team_specialist, name="team_specialist"),
    path('team_admin', BlogListView.as_view(), name='team_admin'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
