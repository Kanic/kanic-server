from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.car_owner == request.user


class IsOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return False
        # return obj.username == request.user.username


class IsOwnerOrAdmin(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        try:
            is_admin = request.user.is_admin
        except AttributeError:
            return False

        return obj.car_owner == request.user or request.user.is_admin
