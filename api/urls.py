from django.urls import path 
from . import views

app_name = 'api'

urlpatterns = [
    path('',
         views.api_root,
         name='api_root'),
    path('stores/',
         views.StoreList.as_view(),
         name='store_list'),
    path('stores/<int:store_pk>/',
         views.StoreDetail.as_view(),
         name='store_detail'),
    path('stores/<int:store_pk>/categories/',
         views.CategoryList.as_view(),
         name='category_list'),
    path('stores/<int:store_pk>/categories/<int:category_pk>/',
         views.StoreCategoryDetail.as_view(),
         name='store_category_detail'),
    path('stores/<int:store_pk>/categories/<int:category_pk>/items/',
         views.ItemList.as_view(),
         name='item_list'),
    path('stores/<int:store_pk>/categories/<int:category_pk>/items/'
         '<int:item_pk>/',
         views.StoreItemDetail.as_view(),
         name='item_detail'),

    # short urls
    path('categories/<int:category_pk>/',
         views.CategoryDetail.as_view(),
         name='category_detail'),
    path('items/<int:item_pk>/',
         views.ItemDetail.as_view(),
         name='item_detail'),
]
