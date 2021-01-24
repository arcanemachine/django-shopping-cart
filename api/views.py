from django.contrib.auth import get_user_model
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from rest_framework import generics
from rest_framework.authtoken.models import Token
from rest_framework.exceptions import PermissionDenied
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from . import serializers
from .permissions import HasStorePermissionsOrReadOnly
from stores.models import Store, Category, Item
from users.models import Profile

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
    permission_classes = [AllowAny]
    serializer_class = serializers.UserSerializer

    def get_object(self):
        if self.request.user.is_authenticated \
                and self.request.user.pk == self.kwargs['user_pk']:
            return get_object_or_404(UserModel, pk=self.kwargs['user_pk'])
        else:
            raise PermissionDenied({'message': "Permission denied."})

    def destroy(self, request, *args, **kwargs):
        return JsonResponse({'message': 'DELETE method not allowed for User'})


class UserTokenDetail(UserDetail):
    """Return a User model that matches the token entered."""

    def get_object(self):
        try:
            auth_header_string = self.request.headers.get('Authorization')
            key = auth_header_string.split(' ')[1]
        except Exception:
            raise ValueError(
                "'Authorization' header and token not found in request.")
        token = get_object_or_404(Token, key=key)
        return token.user


class ProfileDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [AllowAny]
    serializer_class = serializers.ProfileSerializer

    def get_object(self):
        if self.request.user.is_staff or self.request.user.is_authenticated \
                and self.request.user.pk == self.kwargs['user_pk']:
            return get_object_or_404(
                UserModel, pk=self.kwargs['user_pk']).profile

    def destroy(self, request, *args, **kwargs):
        return JsonResponse(
            {'message': 'DELETE method not allowed for Profile'})


class ProfileTokenDetail(ProfileDetail):
    def get_object(self):
        try:
            auth_header_string = self.request.headers.get('Authorization')
            key = auth_header_string.split(' ')[1]
        except Exception:
            raise ValueError(
                "'Authorization' header and token not found in request. ")
        token = get_object_or_404(Token, key=key)
        return token.user.profile


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


# update

class CartDetail(generics.RetrieveAPIView, CheckObjectPermissionsMixin):
    permission_classes = [HasStorePermissionsOrReadOnly]
    serializer_class = serializers.CartSerializer

    def check_permissions(self, request):
        super().check_permissions(request)
        obj = self.get_object()
        super().check_object_permissions(request, obj)

    def get_queryset(self):
        return Profile.objects.filter(pk__in=[self.get_object().pk])

    def get_object(self):
        if self.request.user.is_authenticated:
            return self.request.user.profile
        try:
            auth_header_string = self.request.headers.get('Authorization')
            key = auth_header_string.split(' ')[1]
        except Exception:
            raise ValueError(
                "'Authorization' header and token not found in request.")
        token = get_object_or_404(Token, key=key)
        return token.user.profile


class CartUpdate(generics.UpdateAPIView, CheckObjectPermissionsMixin):
    """/api/v1/[item_id]/[quantity]/

    Use empty POST to add/remove the desired quantity of item_id to the cart.

    Or, the cart value can be manually updated using a "cart" dict.
    """
    permission_classes = [HasStorePermissionsOrReadOnly]
    serializer_class = serializers.CartSerializer

    def check_permissions(self, request):
        super().check_permissions(request)
        obj = self.get_object()
        super().check_object_permissions(request, obj)

    def get_queryset(self):
        return Profile.objects.filter(pk__in=[self.get_object().pk])


    def get_object(self):
        if self.request.user.is_authenticated:
            return self.request.user.profile
        try:
            auth_header_string = self.request.headers.get('Authorization')
            key = auth_header_string.split(' ')[1]
        except Exception:
            raise AttributeError(
                "'Authorization' header and token not found in request.")
        token = get_object_or_404(Token, key=key)
        return token.user.profile

    def get(self, request, *args, **kwargs):
        serializer = self.get_serializer(
            self.get_object(), data=request.data, partial=True)
        if serializer.is_valid():
            pass
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        instance = self.get_object()
        if 'cart' in request.data and type(request.data['cart']) == dict:
            cart = request.data['cart']
            data = request.data
            manual_update = True
        else:
            cart = instance.cart
            data = cart
            manual_update = False
        str_item_pk = str(self.kwargs['item_pk'])
        try:
            quantity = int(self.kwargs['quantity'])
        except ValueError:
            raise ValueError("Quantity must be convertable to an integer.")

        # prevent the API call from succeeding if the item doesn't exist
        get_object_or_404(Item, pk=str_item_pk)

        # determine action type based on the quantity entered (add/remove)
        if not manual_update or request.method == 'GET':
            if quantity == 0:
                return JsonResponse(
                    {'message':
                        'Enter an integer value to add or remove items'})
            elif quantity > 0:
                if str_item_pk in cart.keys():
                    cart[str_item_pk] += quantity
                else:
                    cart[str_item_pk] = quantity
            elif quantity < 0:
                quantity = abs(quantity)
                if str_item_pk not in cart:
                    pass
                elif cart[str_item_pk] - quantity <= 0:
                    del cart[str_item_pk]
                else:
                    cart[str_item_pk] = cart[str_item_pk] - quantity
        serializer = \
            self.get_serializer(instance, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)


class CartClearItem(generics.UpdateAPIView, CheckObjectPermissionsMixin):
    permission_classes = [HasStorePermissionsOrReadOnly]
    serializer_class = serializers.CartSerializer

    def check_permissions(self, request):
        super().check_permissions(request)
        obj = self.get_object()
        super().check_object_permissions(request, obj)

    def get_queryset(self):
        return Profile.objects.filter(pk__in=[self.get_object().pk])

    def get_object(self):
        if self.request.user.is_authenticated:
            return self.request.user.profile
        try:
            auth_header_string = self.request.headers.get('Authorization')
            key = auth_header_string.split(' ')[1]
        except Exception:
            raise ValueError(
                "'Authorization' header and token not found in request.")
        token = get_object_or_404(Token, key=key)
        return token.user.profile

    def post(self, request, *args, **kwargs):
        instance = self.get_object()
        cart = self.instance.cart
        str_item_pk = str(self.kwargs['item_pk'])
        
        # if item is in the cart, remove it
        if str_item_pk in cart:
            del cart[str_item_pk]

        # save the cart info and return the cart
        serializer = \
            self.get_serializer(instance, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)


class CartClearAll(generics.UpdateAPIView, CheckObjectPermissionsMixin):
    permission_classes = [HasStorePermissionsOrReadOnly]
    serializer_class = serializers.CartSerializer

    def check_permissions(self, request):
        super().check_permissions(request)
        obj = self.get_object()
        super().check_object_permissions(request, obj)

    def get_queryset(self):
        return Profile.objects.filter(pk__in=[self.get_object().pk])

    def get_object(self):
        if self.request.user.is_authenticated:
            return self.request.user.profile
        try:
            auth_header_string = self.request.headers.get('Authorization')
            key = auth_header_string.split(' ')[1]
        except Exception:
            raise ValueError(
                "'Authorization' header and token not found in request.")
        token = get_object_or_404(Token, key=key)
        return token.user.profile

    def post(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.cart = {}
        
        # save the cart info and return the cart
        serializer = \
            self.get_serializer(instance, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)

