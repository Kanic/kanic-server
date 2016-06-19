from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.car_owner == request.user


class IsOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return False
        # return obj.username == request.user.username


class IsOwnerOrAdminRequest(permissions.BasePermission):
    def has_permission(self, request, view):
        try:
            is_admin = request.user.is_admin
        except AttributeError:
            return False
        return view.get_object().car_owner == request.user or is_admin


class IsOwnerOrAdminUser(permissions.BasePermission):
    def has_permission(self, request, view):
        try:
            is_admin = request.user.is_admin
        except AttributeError:
            return False
        return view.get_object() == request.user or is_admin
