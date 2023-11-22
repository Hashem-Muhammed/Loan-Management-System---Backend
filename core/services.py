from .models import AmortizationEntry

class LoanService:
    def __init__(self, loan):
        self.loan = loan
        self.number_of_months = loan.term.number_of_months
        self.monthly_rate = loan.interest_rate / 12
        self.amount = loan.amount

    def _calculate_monthly_payment_amount(self):
        self.monthly_payment_amount = (
            self.monthly_rate
            * self.amount
            / (1 - (1 + self.monthly_rate) ** -self.number_of_months)
        )

    def generate_amortization_table(self):
        self._calculate_monthly_payment_amount()
        remaining_balance = self.amount
        for i in range(0, self.number_of_months):
            interest_paid = remaining_balance * self.monthly_rate
            principal_paid = self.monthly_payment_amount - interest_paid
            remaining_balance -= principal_paid
            entry = AmortizationEntry(
                loan=self.loan,
                payment_number=i + 1,
                payment_amount=self.monthly_payment_amount,
                interest_paid=interest_paid,
                principal_paid=principal_paid,
                remaining_balance=remaining_balance,
            )
            entry.save()
