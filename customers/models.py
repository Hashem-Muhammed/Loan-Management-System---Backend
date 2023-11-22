from django.db import models
from django.contrib.auth.models import User
from core.enums import RequestStatus
# Create your models here.


class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    annual_income = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    credit_score = models.PositiveIntegerField(blank=True, null=True)
    notes = models.TextField(blank=True, null=True)
    
    
    def __str__(self):
        return self.user.username

class LoanRequest(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='loan_requests', null=True, blank=True)
    amount = models.DecimalField(max_digits=15, decimal_places=2)
    status = models.CharField(choices=RequestStatus.choices, default=RequestStatus.PENDING , max_length=10)
    term = models.ForeignKey(to='core.LoanTerm', on_delete=models.CASCADE, related_name='loan_requests')
    loan_type = models.ForeignKey(to='bank_personnel.LoanType', on_delete=models.CASCADE, related_name='loan_requests')
    
    
    def __str__(self):
        return f'{self.customer.user.username}, Amount={self.amount}'
    