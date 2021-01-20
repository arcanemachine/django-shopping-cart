from django.http import JsonResponse
from rest_framework import generics

from . import serializers
from .permissions import HasStorePermissionsOrReadOnly
from stores.models import Store, Category, Item


def api_root(request):
    return JsonResponse({'message': 'hello world!'})


# list

class StoreList(generics.ListCreateAPIView):
    queryset = Store.objects.all()
    serializer_class = serializers.StoreSerializer


class StoreCategoryList(generics.ListCreateAPIView):
    serializer_class = serializers.CategorySerializer

    def check_permissions(self, request):
        super().check_permissions(request)
        obj = Store.objects.get(pk=self.kwargs['store_pk'])
        super().check_object_permissions(request, obj)

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
        obj = Store.objects.get(pk=self.kwargs['store_pk'])
        super().check_object_permissions(request, obj)

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['category_pk'] = self.kwargs['category_pk']
        return context

    def get_queryset(self):
        return Item.objects.filter(category=self.kwargs['category_pk'])


# detail

class StoreDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [HasStorePermissionsOrReadOnly]
    serializer_class = serializers.StoreSerializer
    lookup_url_kwarg = 'store_pk'

    def get_queryset(self):
        return Store.objects.filter(pk=self.kwargs['store_pk'])


class CategoryDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [HasStorePermissionsOrReadOnly]
    serializer_class = serializers.CategorySerializer
    lookup_url_kwarg = 'category_pk'

    def check_permissions(self, request):
        super().check_permissions(request)
        obj = self.get_queryset()
        super().check_object_permissions(request, obj)

    def get_queryset(self):
        return Category.objects.filter(pk=self.kwargs['category_pk'])


class ItemDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [HasStorePermissionsOrReadOnly]
    serializer_class = serializers.ItemSerializer
    lookup_url_kwarg = 'item_pk'

    def check_permissions(self, request):
        super().check_permissions(request)
        obj = self.get_queryset()
        super().check_object_permissions(request, obj)

    def get_queryset(self):
        return Item.objects.filter(pk=self.kwargs['item_pk'])
