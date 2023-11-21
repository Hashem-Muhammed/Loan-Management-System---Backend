from rest_framework import permissions
from .models import BankPersonnel

class IsBankPersonnel(permissions.BasePermission):
    def has_permission(self, request, view):
        try:
            bank_personnel = BankPersonnel.objects.get(user=request.user)
            return True
        except BankPersonnel.DoesNotExist:
            return False 
