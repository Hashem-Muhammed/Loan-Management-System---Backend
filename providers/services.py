# from django.core.exceptions import ValidationError
# from bank_personnel.models import LoanFund


# class FundService:
#     def __init__(self, **kwargs):
#         print(kwargs)
#         self.amount = float(kwargs.get("amount")[0])
#         self.loan_fund = kwargs.get("loan_fund")[0]
#         self.max_amount =  self.loan_fund.max_amount
#         self.min_amount = self.loan_fund.min_amount
#         # try:
#         #     self.loan_fund = LoanFund.objects.get(pk=kwargs.get("loan_fund"))
#         #     self.max_amount =  self.loan_fund.max_amount
#         #     self.min_amount = self.loan_fund.min_amount
#         # except LoanFund.DoesNotExist:
#         #     raise ValidationError("LoanFund does not exist or is invalid.")

#     def validate_fund_amount(self):
#         if self.amount > self.max_amount or self.amount < self.min_amount:
#             raise ValidationError(
#                 f"Fund amount should be between {self.min_amount} and {self.max_amount}"
#             )
