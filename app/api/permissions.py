from rest_framework import permissions

from stores.models import Store, Category, Item
from users.models import Profile


class HasStorePermissionsOrReadOnly(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        elif not request.user.is_authenticated:
            return False
        elif request.user.is_staff:
            return True
        elif type(obj) == Profile:
            return obj.user == request.user
        elif type(obj) == Store:
            return obj.registrant == request.user
        elif type(obj) == Category:
            return obj.store.registrant == request.user
        elif type(obj) == Item:
            return obj.category.store.registrant == request.user
        else:
            raise TypeError("This permission can only be used with a "
                            "Store-related object.")
