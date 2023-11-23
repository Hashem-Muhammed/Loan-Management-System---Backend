from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status
from django.contrib.auth.models import User
from core.models import Loan
from .models import BankPersonnel
from core.seed import *


class Helper:
    @staticmethod
    def create_bank_personnel():
        user = User.objects.create(
            username="personnel",
            email="personnel@example.com",
            password="hashem1234",
            first_name="personnel",
        )
        bank_personnel = BankPersonnel.objects.create(user=user)
        return user, bank_personnel


class CreateLoanFundTest(APITestCase):
    def setUp(self):
        self.user, self.bank_personnel = Helper.create_bank_personnel()
        self.url = reverse("create_loan_fund")
        self.client.force_authenticate(user=self.user)

    def test_create_valid_loan_funds(self):
        loan_fund = {
            "name": "buisness",
            "max_amount": 1000000,
            "min_amount": 10000,
            "interest_rate": 0.5,
            "number_of_months": 12,
        }
        response = self.client.post(self.url, loan_fund)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

class CreateLoanType(APITestCase):
    def setUp(self):
        self.user, self.bank_personnel = Helper.create_bank_personnel()
        self.url = reverse("create_loan_type")
        self.client.force_authenticate(user=self.user)
        self.loan_fund = create_loan_fund()
        self.loan_terms =[]
        for _ in range(5):
            loan_term = create_loan_term()
            self.loan_terms.append(loan_term.id)
            
    def test_create_valid_loan_funds(self):
        loan_type= {
            "name": "buisness",
            "max_amount": 1000000,
            "min_amount": 10000,
            "interest_rate": 0.5,
            "number_of_months": 12,
            "loan_fund": self.loan_fund.id,
            "loan_terms":self.loan_terms
        }
        response = self.client.post(self.url, loan_type)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        