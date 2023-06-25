from rest_framework import permissions

class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        
        # Adjust cookie settings based on user authentication
        if request.user.is_authenticated:
            # User is logged in
            SESSION_COOKIE_SAMESITE = 'Lax'
            SESSION_COOKIE_SECURE = False
            CSRF_COOKIE_SAMESITE = 'Lax'
            CSRF_COOKIE_SECURE = False
        else:
            # User is not logged in
            SESSION_COOKIE_SAMESITE = 'None'
            SESSION_COOKIE_SECURE = True
            CSRF_COOKIE_SAMESITE = 'None'
            CSRF_COOKIE_SECURE = True

        return obj.owner == request.user
