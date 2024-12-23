# permissions.py
from rest_framework.permissions import BasePermission, SAFE_METHODS

class IsGuestOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        # Allow read-only for unauthenticated users
        if request.method in SAFE_METHODS:
            return True
        # Check for guest role in token
        return "guest" in request.user.groups.values_list('name', flat=True)

class IsMemberOrAdmin(BasePermission):
    def has_permission(self, request, view):
        # Allow full access for members or admins
        return any(group in ['member', 'administrator'] for group in request.user.groups.values_list('name', flat=True))

class IsAdmin(BasePermission):
    def has_permission(self, request, view):
        # Allow full access for administrators only
        return "administrator" in request.user.groups.values_list('name', flat=True)
    
class IsReviewAuthorOrReadOnly(BasePermission):
    def has_object_permission(self, request, view, obj):
        # SAFE_METHODS are read-only methods like GET, HEAD, OPTIONS
        if request.method in ('GET', 'HEAD', 'OPTIONS'):
            return True
        
        if request.user.is_staff:
            return True

        # Check if the user is the author of the review
        return obj.user == request.user
