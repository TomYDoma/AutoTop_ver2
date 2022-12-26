from django.urls import path, re_path
from django.conf import settings
from django.conf.urls.static import static
from . import views
from .views import (SmecAdminListView, SmecListView, mainCart)

urlpatterns = [
    path('feedback_new', views.createFeedback, name='feedback_new'),
    path('', views.mainCartt, name = "home"),
    path('contact', views.contact, name = "contact"),
    path('services', views.services, name="services"),
    path('team_specialist',SmecListView.as_view(), name="team_specialist"),
    path('team_admin', SmecAdminListView.as_view(), name='team_admin'),
    path('useful', views.useful, name='useful'),
    path('news_filter/<int:pk>', views.news_filter, name="news_filter"),
    path('useful/<int:pk>', views.NewsDetailView.as_view(), name='news-detail'),
    path('comment/<int:pk>', views.createComment, name='comment'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
