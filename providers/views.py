from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from .permissions import IsProvider
from rest_framework.generics import CreateAPIView
from .models import *
from .serializers import *
from .services import *


class CreateFundAPIView(CreateAPIView):
    queryset = Fund.objects.all()
    serializer_class = GenericFundSerializer
    permission_classes = [IsAuthenticated, IsProvider]

    def perform_create(self, serializer):
        serializer.save(provider=Provider.objects.get(user=self.request.user))
