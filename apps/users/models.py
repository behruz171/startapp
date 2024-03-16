from django.db import models
from django.core.validators import RegexValidator
from django.contrib.auth.models import AbstractUser
from django.db import models

PHONE_NUMBER_VALIDATOR = RegexValidator(regex=r"^/+998/d{9}$",message="Invalid phone number")
 
 
 
 
class User(AbstractUser):
    TURLAR = (
        ('Teacher', 'Teacher'),
        ('Director', 'Director'),
    )
    type = models.CharField(max_length=250,
                           choices=TURLAR,
                           default='Teacher',
                           verbose_name="Type")
    
    def __str__(self) -> str:
        return self.type



