from rest_framework import permissions

class IsAdminOrAuthor(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user and request.user.is_authenticated:
            if request.user.is_admin or view.action in ['retrieve', 'list']:
                return True
            if view.action in ['create', 'update', 'partial_update', 'destroy']:
                return request.user.is_author
        return False

    def has_object_permission(self, request, view, obj):
        if request.user.is_admin:
            return True
        return obj.author == request.user
