from django.urls import path

from . import views

app_name = 'api'

urlpatterns = [
    path('', views.api_root, name='api_root'),
    path('stores/', views.StoreList.as_view(), name='store_list'),
]
