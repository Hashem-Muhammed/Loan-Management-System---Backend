from django.urls import path
from .views import *

urlpatterns = [
    path("create-loan-request/", view = CreateLoanRequestAPI.as_view()),

]
