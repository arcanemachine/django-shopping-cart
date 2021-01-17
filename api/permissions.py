from rest_framework import permissions

from stores.models import Store


class HasStorePermissionsOrReadOnly(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        if not request.user.is_authenticated:
            return False
        elif type(obj) is not Store:
            raise TypeError(
                "This permission can only be used with a Store object.")
        elif request.method in permissions.SAFE_METHODS:
            return True
        elif request.user.is_staff:
            return True
        else:
            return request.user in obj.restaurant.admin_users.all()
