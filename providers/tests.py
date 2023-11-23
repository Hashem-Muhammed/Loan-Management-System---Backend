from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status
from django.contrib.auth.models import User
from core.models import Loan
from .models import Provider
from core.seed import *


class Helper:
    @staticmethod
    def create_provider():
        user = User.objects.create(
            username="provider",
            email="provider@example.com",
            password="hashem1234",
            first_name="provider",
        )
        provider = Provider.objects.create(user=user)
        return user, provider


class CreateFundTest(APITestCase):
    def setUp(self):
        self.user, self.provider = Helper.create_provider()
        self.url = reverse("create_fund")
        self.loan_fund = create_loan_fund()
        self.client.force_authenticate(user=self.user)
        self.expected_error = "{{'amount': [ErrorDetail(string='Fund amount should be between {:.2f} and {:.2f}', code='invalid')]}}".format(
            float(self.loan_fund.min_amount), float(self.loan_fund.max_amount)
        )
        self.loan_fund_obj = {
            "provider": self.provider.id,
            "amount": self.loan_fund.max_amount,
            "loan_fund": self.loan_fund.id,
        }

    def test_create_valid_fund(self):
        self.loan_fund_obj["amount"] = self.loan_fund_obj["amount"] - 1
        response = self.client.post(self.url, self.loan_fund_obj)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_fund_with_amount_eq_loan_fund_max_amount(self):
        self.loan_fund_obj["amount"] = self.loan_fund.max_amount 
        response = self.client.post(self.url, self.loan_fund_obj)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    
    def test_create_fund_with_amount_eq_loan_fund_min_amount(self):
        self.loan_fund_obj["amount"] = self.loan_fund.min_amount 
        response = self.client.post(self.url, self.loan_fund_obj)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_fund_with_amount_lt_loan_fund_min_amount(self):
        self.loan_fund_obj["amount"] = self.loan_fund.min_amount - 1
        response = self.client.post(self.url, self.loan_fund_obj)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(str(response.data), self.expected_error)

    def test_create_fund_with_amount_lt_loan_fund_max_amount(self):
        self.loan_fund_obj["amount"] = self.loan_fund.max_amount + 1
        response = self.client.post(self.url, self.loan_fund_obj)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(str(response.data), self.expected_error)
