from rest_framework import serializers
from .models import *


class AmortizationEntrySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = AmortizationEntry
        fields = '__all__'
    