from django.urls import path
from .views import *

urlpatterns = [
    path("create-loan-request/", view = CreateLoanRequestAPI.as_view()),
    path("get-amortized-table/", view = get_amortized_table_by_loan_id),
        

]
