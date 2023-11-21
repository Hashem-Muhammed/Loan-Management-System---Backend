from django.urls import path
from .views import *

urlpatterns = [
    path("create-loan-fund/", view = CreateLoanFundAPIView.as_view()),

]
