
class FundService:
    def __init__(self, amount, loan_fund):
        self.amount = amount
        self.loan_fund = loan_fund
        self.max_amount = self.loan_fund.max_amount
        self.min_amount = self.loan_fund.min_amount

    def validate_fund_amount(self):
        return self.amount <= self.max_amount and self.amount >= self.min_amount
