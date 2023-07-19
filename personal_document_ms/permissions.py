from rest_framework import permissions

class IsAdminOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user.role == 1
    
class IsOwnerOrAdminOnly(permissions.BasePermission):
    message = "Admin or Object Owner is allowed to perform this action"

    def has_permission(self, request, view):
        return request.user.role == 1 or request.user.role ==2
    
    def has_object_permission(self, request, view, obj):
        return obj.owner == request.user or request.user.role == 1