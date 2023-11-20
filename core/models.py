from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from providers.models import Provider
from customers.models import Customer


class LoanFund(models.Model):
    amount = models.DecimalField(max_digits=15, decimal_places=2, null=True, blank=True)
    max_amount = models.DecimalField(max_digits=15, decimal_places=2, null=True, blank=True)
    min_amount = models.DecimalField(max_digits=15, decimal_places=2, null=True, blank=True)
    interest_rate = models.FloatField(null=True, blank=True, validators=[
            MinValueValidator(0.0),
            MaxValueValidator(100.0), 
        ] )
    provider = models.ForeignKey(Provider, null=True , blank=True , on_delete=models.CASCADE)
    
    def __str__(self):
        return self.amount


class LoanTerm(models.Model):
    interest_rate = models.FloatField(validators=[
            MinValueValidator(0.0),
            MaxValueValidator(100.0), 
        ])
    number_of_months =models.IntegerField()
    
    def __str__(self):
        return f'{self.number_of_months} months, interest rate= {self.interest_rate}'
        
        
class Loan(models.Model):
    loan_fund = models.ForeignKey(LoanFund, on_delete=models.CASCADE, related_name='loans')
    amount = models.DecimalField(max_digits=15, decimal_places=2)
    interest_rate = models.FloatField(validators=[
            MinValueValidator(0.0),
            MaxValueValidator(100.0), 
        ])
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='loans')
    term = models.ForeignKey(LoanTerm, on_delete=models.CASCADE, related_name='loans')
    
    def __str__(self):
        return f'{self.customer.user.username}, {self.amount}'