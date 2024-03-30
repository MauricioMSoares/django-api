from rest_framework import permissions

class IsUserOwnerOrGetAndPostOnly(permissions.BasePermission):
    """
    Custom permissions for the UserViewSet to only allow users to edit their own user. Otherwise, Get and Post only.
    """

    def has_permission(self, request, view):
        return True

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        
        if not request.user.is_anonymous:
            return request.user == obj

        return False
    

class IsProfileOwnerOrReadOnly(permissions.BasePermission):
    """
    Custom permissions for the ProfileViewSet to only allow users to edit their own profile. Otherwise, Get and Post only.
    """

    def has_permission(self, request, view):
        return True
    
    def has_object_permission(self, request, view, obj):
        if request.method is permissions.SAFE_METHODS:
            return True
        
        if not request.user.is_anonymous:
            return request.user.profile == obj
        
        return False
