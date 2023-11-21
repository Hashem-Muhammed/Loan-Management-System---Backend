from rest_framework import permissions
from .models import Provider

class IsProvider(permissions.BasePermission):
    def has_permission(self, request, view):
        try:
            provider = Provider.objects.get(user=request.user)
            return True
        except Provider.DoesNotExist:
            return False 
