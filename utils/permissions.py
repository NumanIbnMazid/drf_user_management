from rest_framework import permissions


class IsStaff(permissions.BasePermission):
    """
    Permission: IsStaff
    """

    message = "`IsStaff` permission required."

    def has_permission(self, request, view):
        """
        Return `True` if permission is granted, `False` otherwise.
        """
        if not bool(request.user and request.user.is_authenticated):
            return False
        if request.user.is_superuser or request.user.is_staff:
            return True
        return False

    def has_object_permission(self, request, view, obj):
        if not bool(request.user and request.user.is_authenticated):
            return False

        if request.user.is_superuser or request.user.is_staff:
            return True
        return False


class IsSuperUser(permissions.BasePermission):
    """
    Permission: IsSuperUser
    """

    message = "`IsSuperUser` permission required."

    def has_permission(self, request, view):
        """
        Return `True` if permission is granted, `False` otherwise.
        """
        if not bool(request.user and request.user.is_authenticated):
            return False
        if request.user.is_superuser:
            return True
        return False

    def has_object_permission(self, request, view, obj):
        if not bool(request.user and request.user.is_authenticated):
            return False

        if request.user.is_superuser:
            return True
        return False
