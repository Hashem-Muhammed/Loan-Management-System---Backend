from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator


class BankPersonnel(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.user.username
    

class LoanFund(models.Model):
    name = models.CharField(max_length=255)
    max_amount = models.DecimalField(max_digits=15, decimal_places=2)
    min_amount = models.DecimalField(max_digits=15, decimal_places=2)
    interest_rate = models.FloatField(null=True, blank=True, validators=[
            MinValueValidator(0.0),
            MaxValueValidator(100.0), 
        ] )
    number_of_months =models.PositiveBigIntegerField(validators=[MinValueValidator(0)])
    
    
    def __str__(self):
        return self.name
    
    
class LoanType(models.Model):
    name = models.CharField(max_length=200)
    max_amount = models.DecimalField(max_digits=15, decimal_places=2, null=True, blank=True)
    min_amount = models.DecimalField(max_digits=15, decimal_places=2, null=True, blank=True)
    loan_terms = models.ManyToManyField(to='core.LoanTerm')
    loan_fund = models.ForeignKey(LoanFund, on_delete=models.CASCADE, related_name='loan_types')