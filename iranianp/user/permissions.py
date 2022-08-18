from rest_framework import permissions


class UserPermission(permissions.BasePermission):

    def has_permission(self, request, view):
        # only superuser can access to all user detail
        if view.action=='list':
            return bool(request.user.is_authenticated and request.user.is_superuser)
        # everyone can create
        elif view.action=='create':
            return True
