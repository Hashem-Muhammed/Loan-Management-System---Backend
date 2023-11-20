from django.db import models

class RequestStatus(models.TextChoices):
    PENDING = 'PENDING'
    ACCEPTED = 'ACCEPTED'
    REJECTED = 'REJECTED'