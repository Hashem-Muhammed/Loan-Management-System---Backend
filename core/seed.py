import random
from faker import Faker
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.core.validators import MinValueValidator, MaxValueValidator
from django.core.exceptions import ValidationError
from django.db import models
from .models import *
from providers.models import *
from customers.models import *
from bank_personnel.models import *

fake = Faker()

def create_user():
    username = fake.user_name()
    email = fake.email()
    password = fake.password()
    user = User.objects.create_user(username=username, email=email, password=password)
    return user

def create_customer():
    user = create_user()
    annual_income = random.randint(20000, 150000)
    credit_score = random.randint(300, 850)
    notes = fake.text()
    customer = Customer.objects.create(user=user, annual_income=annual_income, credit_score=credit_score, notes=notes)
    return customer

def create_loan_term():
    number_of_months = random.randint(6, 36)
    loan_term = LoanTerm.objects.create(number_of_months=number_of_months)
    return loan_term

def create_loan():
    loan_type = create_loan_type()
    amount = random.randint(5000, 50000)
    interest_rate = random.randint(1, 10)
    customer = create_customer()
    term = create_loan_term()
    loan = Loan.objects.create(loan_type=loan_type, amount=amount, interest_rate=interest_rate, customer=customer, term=term)
    return loan

def create_loan_type():
    name = fake.word()
    max_amount = random.randint(10000, 50000)
    min_amount = random.randint(1000, 5000)
    interest_rate = random.randint(1, 10)
    loan_fund = create_loan_fund()
    loan_term = create_loan_term()
    loan_type = LoanType.objects.create(
        name=name,
        max_amount=max_amount,
        min_amount=min_amount,
        interest_rate=interest_rate,
        loan_fund=loan_fund
    )
    loan_type.loan_terms.add(loan_term)
    return loan_type

def create_loan_fund():
    name = fake.word()
    max_amount = random.randint(50000, 100000)
    min_amount = random.randint(10000, 50000)
    interest_rate = random.randint(1, 5)
    number_of_months = random.randint(12, 120)
    loan_fund = LoanFund.objects.create(
        name=name,
        max_amount=max_amount,
        min_amount=min_amount,
        interest_rate=interest_rate,
        number_of_months=number_of_months
    )
    return loan_fund

def create_bank_personnel():
    user = create_user()
    bank_personnel = BankPersonnel.objects.create(user=user)
    return bank_personnel

def create_fund():
    amount = random.randint(100000, 500000)
    provider = create_provider()
    loan_fund = create_loan_fund()
    fund = Fund.objects.create(amount=amount, provider=provider, loan_fund=loan_fund)
    return fund

def create_provider():
    user = create_user()
    provider = Provider.objects.create(user=user)
    return provider

def create_loan_request():
    customer = create_customer()
    amount = random.randint(5000, 50000)
    term = create_loan_term()
    loan_type = create_loan_type()
    loan_request = LoanRequest.objects.create(
        customer=customer,
        amount=amount,
        term=term,
        loan_type=loan_type
    )
    return loan_request

def seed_data():
    for _ in range(5):  
        create_loan()
        create_customer()
        create_loan_term()
        create_loan_type()
        create_loan_fund()
        create_bank_personnel()
        create_fund()
        create_provider()
        create_loan_request()


