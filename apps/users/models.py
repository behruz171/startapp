from django.db import models
from django.core.validators import RegexValidator
from django.contrib.auth.models import AbstractUser
from django.db import models
from rest_framework_simplejwt.tokens import RefreshToken
from apps.common.models import *


PHONE_NUMBER_VALIDATOR = RegexValidator(regex=r"^\+998\d{9}$",message="Invalid phone number")
 
 
 
class User(AbstractUser):
    TURLAR = (
        ('Teacher', 'Teacher'),
        ('Director', 'Director'),
        ('Admin', 'Admin')
    )
    type = models.CharField(max_length=250,
                            choices=TURLAR,
                            default='Teacher',
                            verbose_name="Type")

    phone_number = models.CharField(max_length=13,
                                    validators=[PHONE_NUMBER_VALIDATOR],
                                    verbose_name='Phone number')
    experience = models.IntegerField(default=0,
                                      verbose_name='Experience')
    birthday = models.DateField(null=True)

    def __str__(self) -> str:
        return self.type

    def tokens(self):
        refresh = RefreshToken.for_user(self)

        return {
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        }


