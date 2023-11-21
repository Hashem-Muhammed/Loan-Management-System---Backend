from rest_framework import serializers
from .models import *


class LoanFundSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = LoanFund
        fields = '__all__'
        
