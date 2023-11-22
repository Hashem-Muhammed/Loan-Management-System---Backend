from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from providers.models import Provider
from customers.models import Customer
from bank_personnel.models import LoanFund
 

class LoanTerm(models.Model):
    interest_rate = models.FloatField(validators=[
            MinValueValidator(0.0),
            MaxValueValidator(100.0), 
        ])
    number_of_months =models.IntegerField()
    
    def __str__(self):
        return f'{self.number_of_months} months, interest rate= {self.interest_rate}'




    

        
class Loan(models.Model):
    loan_type = models.ForeignKey(to='bank_personnel.LoanType', on_delete=models.CASCADE, related_name='loans')
    amount = models.DecimalField(max_digits=15, decimal_places=2)
    interest_rate = models.FloatField(validators=[
            MinValueValidator(0.0),
            MaxValueValidator(100.0), 
        ])
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='loans')
    term = models.ForeignKey(LoanTerm, on_delete=models.CASCADE, related_name='loans')
    
    def __str__(self):
        return f'{self.customer.user.username}, {self.amount}'