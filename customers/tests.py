from rest_framework.test import APITestCase
from .views import get_amortized_table_by_loan_id
from django.urls import reverse
from rest_framework import status
from django.contrib.auth.models import User
from core.models import Loan
from .models import Customer
from core.seed import *


class Helper:
    @staticmethod
    def create_customer():
        user = User.objects.create(
            username="customer",
            email="customer@example.com",
            password="hashem1234",
            first_name="customer",
        )
        customer = Customer.objects.create(user=user)
        return user, customer


class AmortizedTableTest(APITestCase):
    def setUp(self):
        self.url = reverse("get_amortized_table")
        self.loan_id = Loan.objects.filter(amount__gt=1000).values("id").first()
        self.user, self.customer = Helper.create_customer()
        seed_data()
        self.client.force_authenticate(user=self.user)

    def test_get_amortized_table_with_loan_id(self):
        response = self.client.get(f"{self.url}?loan_id={1}")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, [])

    def test_get_amortized_table_without_loan_id(self):
        response = self.client.get(self.url)
        expected_error = {"error": 'Parameter "loan_id" is required.'}
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data, expected_error)


class CreateLoanRequestTest(APITestCase):
    def setUp(self):
        self.user, self.customer = Helper.create_customer()
        self.url = reverse("create_loan_request")
        self.client.force_authenticate(user=self.user)
        self.loan_type = create_loan_type()
        self.expected_error = "{{'amount': [ErrorDetail(string='The amount you entered for the loan should be in range {:.2f} : {:.2f}.', code='invalid')]}}".format(
            float(self.loan_type.min_amount), float(self.loan_type.max_amount)
        )

    def test_create_valid_loan_request(self):
        loan_request = {
            "customer": self.customer.id,
            "amount": self.loan_type.max_amount - 1,
            "term": self.loan_type.loan_terms.first().id,
            "loan_type": self.loan_type.id,
        }
        response = self.client.post(self.url, loan_request)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_loan_request_with_amount_lt_loan_type_min_amount(self):
        loan_request = {
            "customer": self.customer.id,
            "amount": self.loan_type.min_amount - 1,
            "term": self.loan_type.loan_terms.first().id,
            "loan_type": self.loan_type.id,
        }
        response = self.client.post(self.url, loan_request)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(str(response.data), self.expected_error)

    def test_create_loan_request_with_amount_gt_loan_type_min_amount(self):
        loan_request = {
            "customer": self.customer.id,
            "amount": self.loan_type.max_amount + 1,
            "term": self.loan_type.loan_terms.first().id,
            "loan_type": self.loan_type.id,
        }
        response = self.client.post(self.url, loan_request)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(str(response.data), self.expected_error)

