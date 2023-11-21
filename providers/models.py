from django.db import models, IntegrityError
from django.contrib.auth.models import User
from bank_personnel.models import LoanFund
from django.db.models import CheckConstraint, Q, F
from django.core.exceptions import ValidationError

# Create your models here.



class Provider(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='provider')

    def __str__(self):
        return self.user.username
    
    
class Fund(models.Model):
    amount = models.DecimalField(max_digits=15, decimal_places=2)
    provider = models.ForeignKey(Provider, null=True , blank=True , on_delete=models.CASCADE)
    loan_fund = models.ForeignKey(LoanFund, on_delete=models.CASCADE, related_name='funds')
    
    def __str__(self):
        return f'{self.amount}'
    