from rest_framework import serializers
from .models import *
from .services import CustomerService
from core.models import LoanTerm
from providers.models import LoanFund
from bank_personnel.models import LoanType 


class GenericLoanRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = LoanRequest
        fields = "__all__"


class PostLoanRequestSerializer(GenericLoanRequestSerializer):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setup_customer_service_instance()

    def setup_customer_service_instance(self):
        try:
            term_id = int(self.initial_data.get("term"))
            loan_type_id = int(self.initial_data.get("loan_type"))
            self.amount = self.initial_data.get("amount")
            self.term = LoanTerm.objects.get(pk=term_id)
            self.loan_type = LoanType.objects.get(pk=loan_type_id)
            loan_fund = self.loan_type.loan_fund

            self.customer_service = CustomerService(
                loan_type=self.loan_type,
                term=self.term,
                amount=self.amount,
                loan_fund=loan_fund,
            )
        except ValueError:
            raise serializers.ValidationError(
                "term, loan_type, amount: Incorrect type. received str."
            )
        except LoanTerm.DoesNotExist:
            raise serializers.ValidationError("Term does not exist or is invalid.")
        except LoanType.DoesNotExist:
            raise serializers.ValidationError("loan_type does not exist or is invalid.")

    def validate_term(self, value):
        if not self.customer_service.validate_loan_term():
            raise serializers.ValidationError(
                "The term you entered for the loan is not in this loan terms."
            )

        return value

    def validate_amount(self, value):
        if not self.customer_service.validate_amount():
            raise serializers.ValidationError(
                f"The amount you entered for the loan should be in range {self.loan_type.min_amount} : {self.loan_type.max_amount}."
            )
        return value
