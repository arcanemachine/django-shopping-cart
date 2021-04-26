from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

from . import views
from django_shopping_cart import server_config

urlpatterns = [
    # experimental views
    path('', views.project_root, name='project_root'),
    # path('hello-cookie/', views.hello_cookie, name='hello_cookie'),
    # path('get_csrftoken/', views.get_csrftoken, name='get_csrftoken'),

    path('admin/', admin.site.urls),
    path('users/', include('users.urls')),
    path('api/v1/', include('api.urls')),
    path('api/rest-auth/', include('dj_rest_auth.urls')),
    path('api-auth/', include('rest_framework.urls')),
]

if server_config.SERVER_NAME == 'dev':
    urlpatterns += \
        static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += \
        static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
