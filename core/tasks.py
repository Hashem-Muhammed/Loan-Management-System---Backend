# tasks.py
from celery import shared_task
from django.utils import timezone
from .models import  Loan
from .enums import RequestStatus
from customers.models import LoanRequest
from .services import LoanService
from django.db import models


@shared_task
def process_pending_loan_requests():
    pending_requests = LoanRequest.objects.filter(status=RequestStatus.PENDING)
    print("RUNN")
    for request in pending_requests:
        try:
            available_funds = request.loan_type.loan_fund.funds.aggregate(total_amount=models.Sum('amount'))['total_amount'] or 0
            print(available_funds)
            if available_funds >= request.amount:
                request.status = RequestStatus.ACCEPTED.value
                request.save()

                loan = Loan.objects.create(
                    loan_type=request.loan_type,
                    amount=request.amount,
                    interest_rate=request.loan_type.interest_rate,
                    customer=request.customer,
                    term=request.term,
                )
                loan_service = LoanService(loan)
                loan_service.generate_amortization_table()
        except Exception as e:
            print(f"Error processing loan request {request.id}: {e}")
            
