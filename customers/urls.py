from django.urls import path
from .views import *

urlpatterns = [
    path("create-loan-request/", view = CreateLoanRequestAPI.as_view(), name='create_loan_request'),
    path("get-amortized-table/", view = get_amortized_table_by_loan_id, name='get_amortized_table'),
]
