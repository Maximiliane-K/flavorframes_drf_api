from rest_framework import permissions

class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Custom permission to allow only owners
    to edit or delete the object.
    """
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        if hasattr(obj, 'owner'):
            return obj.owner == request.user
        elif hasattr(obj, 'follower'):
            return obj.follower == request.user
        else:
            return False  