from rest_framework import permissions


class IsActive(permissions.BasePermission):
    """Метод проверяет, является ли user активным."""

    def has_object_permission(self, request, view, obj):
        if obj.is_active:
            return True
        return False
