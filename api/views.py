from django.contrib.auth import get_user_model
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from rest_framework import generics
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny

from . import serializers
from .permissions import HasStorePermissionsOrReadOnly
from stores.models import Store, Category, Item

UserModel = get_user_model()


class CheckObjectPermissionsMixin:
    def check_permissions(self, request):
        super().check_permissions(request)
        obj = Store.objects.get(pk=self.kwargs['store_pk'])
        super().check_object_permissions(request, obj)


def api_root(request):
    return JsonResponse({'message': 'hello world!'})


# list

class StoreList(generics.ListCreateAPIView):
    queryset = Store.objects.all()
    serializer_class = serializers.StoreSerializer


class StoreCategoryList(generics.ListCreateAPIView):
    serializer_class = serializers.CategorySerializer

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['store_pk'] = self.kwargs['store_pk']
        return context

    def get_queryset(self):
        return Category.objects.filter(store=self.kwargs['store_pk'])


class CategoryItemList(generics.ListCreateAPIView):
    serializer_class = serializers.ItemSerializer

    def check_permissions(self, request):
        super().check_permissions(request)
        obj = self.get_queryset()
        super().check_object_permissions(request, obj)

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['category_pk'] = self.kwargs['category_pk']
        return context

    def get_queryset(self):
        return Item.objects.filter(category=self.kwargs['category_pk'])


class CartItemList(generics.ListCreateAPIView):
    serializer_class = serializers.ItemSerializer

    def check_permissions(self, request):
        super().check_permissions(request)
        obj = self.get_queryset()
        super().check_object_permissions(request, obj)

    def get_queryset(self):
        item_csv_string = self.kwargs['item_csv_string'].split(',')
        return Item.objects.filter(pk__in=item_csv_string)


# detail

class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    """Return a User model that matches the token entered."""
    permission_classes = [AllowAny]
    serializer_class = serializers.UserSerializer

    def get_object(self):
        try:
            auth_header_string = self.request.headers.get('Authorization')
            key = auth_header_string.split(' ')[1]
        except:
            raise ValueError(
                "'Authorization' header and token not found in request.")
        token = get_object_or_404(Token, key=key)
        return token.user

    def destroy(self, request, *args, **kwargs):
        return JsonResponse({'message': 'DELETE method not allowed for User'})


class ProfileDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [AllowAny]
    serializer_class = serializers.ProfileSerializer

    def get_object(self):
        try:
            auth_header_string = self.request.headers.get('Authorization')
            key = auth_header_string.split(' ')[1]
        except:
            raise ValueError(
                "'Authorization' header and token not found in request.")
        token = get_object_or_404(Token, key=key)
        return token.user.profile

    def destroy(self, request, *args, **kwargs):
        return JsonResponse(
            {'message': 'DELETE method not allowed for Profile'})


class StoreDetail(
        generics.RetrieveUpdateDestroyAPIView, CheckObjectPermissionsMixin):
    permission_classes = [HasStorePermissionsOrReadOnly]
    serializer_class = serializers.StoreSerializer
    lookup_url_kwarg = 'store_pk'

    def get_queryset(self):
        return Store.objects.filter(pk=self.kwargs['store_pk'])


class CategoryDetail(
        generics.RetrieveUpdateDestroyAPIView, CheckObjectPermissionsMixin):
    permission_classes = [HasStorePermissionsOrReadOnly]
    serializer_class = serializers.CategorySerializer
    lookup_url_kwarg = 'category_pk'

    def check_permissions(self, request):
        super().check_permissions(request)
        obj = self.get_queryset()
        super().check_object_permissions(request, obj)

    def get_queryset(self):
        return Category.objects.filter(pk=self.kwargs['category_pk'])


class ItemDetail(
        generics.RetrieveUpdateDestroyAPIView, CheckObjectPermissionsMixin):
    permission_classes = [HasStorePermissionsOrReadOnly]
    serializer_class = serializers.ItemSerializer
    lookup_url_kwarg = 'item_pk'

    def check_permissions(self, request):
        super().check_permissions(request)
        obj = self.get_queryset()
        super().check_object_permissions(request, obj)

    def get_queryset(self):
        return Item.objects.filter(pk=self.kwargs['item_pk'])
