from django.urls import path
from .views import *

urlpatterns = [
    path("create-loan-fund/", view = CreateLoanFundAPIView.as_view(), name='create_loan_fund'),
    path("create-loan-type/", view = CreateLoanTypeAPIView.as_view(), name='create_loan_type')
    

]
