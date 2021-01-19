from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

from . import views
from django_shopping_cart import server_config

urlpatterns = [
    path('', views.project_root, name='project_root'),
    path('admin/', admin.site.urls),
    path('users/', include('users.urls')),
    path('api/v1/', include('api.urls')),
    path('api-auth/', include('rest_framework.urls')),
]

if server_config.SERVER_NAME == 'dev':
    urlpatterns += \
        static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += \
        static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
