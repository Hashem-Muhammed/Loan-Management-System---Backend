from django.urls import path
from .views import *

urlpatterns = [
    path("create-fund/", view = CreateFundAPIView.as_view(), name='create_fund'),

]
