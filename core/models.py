from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from providers.models import Provider
from customers.models import Customer
from bank_personnel.models import LoanFund
 

class LoanTerm(models.Model):
    number_of_months =models.IntegerField()
    
    def __str__(self):
        return f'{self.number_of_months} months'


       
class Loan(models.Model):
    loan_type = models.ForeignKey(to='bank_personnel.LoanType', on_delete=models.CASCADE, related_name='loans')
    amount = models.DecimalField(max_digits=15, decimal_places=2)
    interest_rate = models.DecimalField(validators=[
            MinValueValidator(0.0),
            MaxValueValidator(100.0), 
        ], max_digits=8, decimal_places=2)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='loans')
    term = models.ForeignKey(LoanTerm, on_delete=models.CASCADE, related_name='loans')
    
    def __str__(self):
        return f'{self.customer.user.username}, {self.amount}'
    
    
    
class AmortizationEntry(models.Model):
    loan = models.ForeignKey(Loan, on_delete=models.CASCADE, related_name='amortization_entries')
    payment_number = models.IntegerField()
    payment_amount = models.DecimalField(max_digits=10, decimal_places=2)
    interest_paid = models.DecimalField(max_digits=8, decimal_places=2)
    principal_paid = models.DecimalField(max_digits=8, decimal_places=2)
    remaining_balance = models.DecimalField(max_digits=12, decimal_places=2)

    def __str__(self):
        return f"AmortizationEntry #{self.id} for user {self.loan.customer.user.username}, Payment #{self.payment_number}"