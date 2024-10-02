from rest_framework.permissions import BasePermission


class IsAuthorUser(BasePermission):
    """
    Allows access only to admin users.
    """

    def has_permission(self, request, view):
        return bool(
            request.user and request.user.is_author or request.user.is_superuser
        )
