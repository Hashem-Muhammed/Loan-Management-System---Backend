from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from .permissions import IsCustomer
from rest_framework.generics import CreateAPIView
from .models import *
from .serializers import *
from .services import *


class CreateLoanRequestAPI(CreateAPIView):
    queryset = LoanRequest.objects.all()
    serializer_class = PostLoanRequestSerializer
    permission_classes = [IsAuthenticated, IsCustomer]

    def perform_create(self, serializer):
        serializer.save(customer=Customer.objects.get(user=self.request.user))
