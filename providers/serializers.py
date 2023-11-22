from rest_framework import serializers
from .models import *
from .services import FundService


class GenericFundSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fund
        fields = "__all__"


class PostFundSerializer(GenericFundSerializer):
    def validate_amount(self, value):
        try:
            loan_fund_id = int(self.initial_data.get("loan_fund"))
        except ValueError:
            raise serializers.ValidationError(
                "loan_fund: Incorrect type. Expected pk value, received str."
            )
        try:
            loan_fund = LoanFund.objects.get(pk=loan_fund_id)
        except LoanFund.DoesNotExist:
            raise serializers.ValidationError("LoanFund does not exist or is invalid.")
        fund_service = FundService(value, loan_fund)
        if not fund_service.validate_fund_amount():
            raise serializers.ValidationError(
                f"Fund amount should be between {loan_fund.min_amount} and {loan_fund.max_amount}"
            )

        return value
