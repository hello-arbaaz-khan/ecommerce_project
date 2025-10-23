from rest_framework.permissions import BasePermission, SAFE_METHODS

class IsAdminOrReadOnly(BasePermission):
    """
    Allow read (GET) requests to everyone,
    but only admins can modify (POST, PUT, DELETE).
    """
    def has_permission(self, request, view):
        # only allow read-only methods for non-admin users
        if request.method in SAFE_METHODS:
            return True
        # Check if the user is admin for write permissions
        return request.user and request.user.is_staff
    