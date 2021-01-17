from django.http import JsonResponse
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from . import serializers
from .permissions import HasStorePermissionsOrReadOnly
from stores.models import Store, Category, Item


def api_root(request):
    return JsonResponse({'message': 'hello world!'})


class StoreList(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Store.objects.all()
    serializer_class = serializers.StoreSerializer
