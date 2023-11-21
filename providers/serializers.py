from rest_framework import serializers
from .models import *

class GenericFundSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Fund
        fields = '__all__'
    
    def validate_amount(self, value):
        loan_fund_id = self.initial_data.get("loan_fund")
        
        try:
            loan_fund = LoanFund.objects.get(pk=loan_fund_id)
        except LoanFund.DoesNotExist:
            raise serializers.ValidationError("LoanFund does not exist or is invalid.")

        if value > loan_fund.max_amount or value < loan_fund.min_amount:
            raise serializers.ValidationError(
                f"Fund amount should be between {loan_fund.min_amount} and {loan_fund.max_amount}"
            )

        return value