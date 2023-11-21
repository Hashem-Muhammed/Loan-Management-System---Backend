from rest_framework import permissions
from .models import Customer

class IsCustomer(permissions.BasePermission):
    def has_permission(self, request, view):
        try:
            customer = Customer.objects.get(user=request.user)
            return True
        except Customer.DoesNotExist:
            return False 
