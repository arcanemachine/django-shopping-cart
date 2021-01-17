from rest_framework import permissions

from stores.models import Store, Category, Item


class HasStorePermissionsOrReadOnly(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        if not request.user.is_authenticated:
            return False
        elif request.method in permissions.SAFE_METHODS:
            return True
        elif request.user.is_staff:
            return True
        elif type(obj) == Store:
            return obj.user == request.user
        elif type(obj) == Category:
            return obj.store.user == request.user
        elif type(obj) == Item:
            return obj.category.store.user == request.user
        else:
            raise TypeError("This permission can only be used with a "
                            "Store-related object.")
