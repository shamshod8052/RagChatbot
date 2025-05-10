from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include, re_path
from django.views.static import serve

from Control.views import update_info_order

urlpatterns = [
    path("admin/", admin.site.urls, name='admin'),
    path("", include("Control.urls"), name='control'),
    path('update-info-order/', update_info_order, name='update_info_order'),
]

urlpatterns += [re_path(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT})]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
