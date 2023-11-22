from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from .permissions import IsBankPersonnel
from rest_framework.generics import CreateAPIView
from .models import *
from .serializers  import *
from bank_personnel.models import LoanType

class CreateLoanFundAPIView(CreateAPIView):
    queryset = LoanFund.objects.all()
    serializer_class = LoanFundSerializer
    permission_classes = [IsAuthenticated, IsBankPersonnel]
    
class CreateLoanTypeAPIView(CreateAPIView):
    queryset = LoanType.objects.all()
    serializer_class = LoanTypeSerializer
    permission_classes = [IsAuthenticated, IsBankPersonnel]