from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from .permissions import IsBankPersonnel
from rest_framework.generics import CreateAPIView
from .models import *
from .serializers  import *

class CreateLoanFundAPIView(CreateAPIView):
    queryset = LoanFund.objects.all()
    serializer_class = LoanFundSerializer
    permission_classes = [IsAuthenticated, IsBankPersonnel]