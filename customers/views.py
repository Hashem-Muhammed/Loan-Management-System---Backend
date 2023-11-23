from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from .permissions import IsCustomer
from rest_framework.generics import CreateAPIView
from .models import *
from .serializers import *
from .services import *
from core.models import AmortizationEntry
from core.serializers import AmortizationEntrySerializer
from core.services import *


class CreateLoanRequestAPI(CreateAPIView):
    queryset = LoanRequest.objects.all()
    serializer_class = PostLoanRequestSerializer
    permission_classes = [IsAuthenticated, IsCustomer]

    def perform_create(self, serializer):
        serializer.save(customer=Customer.objects.get(user=self.request.user))

@api_view(["GET"])
@permission_classes([IsAuthenticated, IsCustomer])
def get_amortized_table_by_loan_id(request):
    loan_id = request.query_params.get('loan_id', None) 
    if not loan_id:
            return Response({'error': 'Parameter "loan_id" is required.'}, status=status.HTTP_400_BAD_REQUEST)
    queryset = AmortizationEntry.objects.filter(loan=loan_id)
    serializer = AmortizationEntrySerializer(queryset, many=True)
    
    return Response(serializer.data, status=status.HTTP_200_OK)
        
