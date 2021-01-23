from django.urls import path 
from . import views

app_name = 'api'

urlpatterns = [
    path('',
         views.api_root,
         name='api_root'),

    # list
    path('stores/',
         views.StoreList.as_view(),
         name='store_list'),
    path('stores/<int:store_pk>/categories/',
         views.StoreCategoryList.as_view(),
         name='store_category_list'),
    path('categories/<int:category_pk>/items/',
         views.CategoryItemList.as_view(),
         name='item_list'),

    # detail
    path('user/',
         views.UserDetail.as_view(),
         name='user_detail'),
    path('user/profile/',
         views.ProfileDetail.as_view(),
         name='profile_detail'),
    path('stores/<int:store_pk>/',
         views.StoreDetail.as_view(),
         name='store_detail'),
    path('categories/<int:category_pk>/',
         views.CategoryDetail.as_view(),
         name='category_detail'),
    path('items/<int:item_pk>/',
         views.ItemDetail.as_view(),
         name='item_detail'),
]
