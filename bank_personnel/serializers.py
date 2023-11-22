from rest_framework import serializers
from .models import *


class LoanFundSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = LoanFund
        fields = '__all__'
        
class LoanTypeSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = LoanType
        fields = '__all__'
        
