
class CustomerService:
    def __init__(self, loan_type, term, amount, loan_fund ):
        self.loan_type = loan_type
        self.term = term
        self.amount = float(amount)
        self.loan_fund = loan_fund
        
    def validate_loan_term(self):
        return self.term in self.loan_type.loan_terms.all()

    def validate_amount(self):
        return self.amount >= self.loan_type.min_amount and self.amount <= self.loan_type.max_amount