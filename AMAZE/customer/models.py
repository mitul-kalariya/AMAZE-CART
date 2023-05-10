from django.db import models
from django.contrib.auth.models import AbstractUser


class customer(AbstractUser):
    genders = [('MALE','MALE'),('FEMALE','FEMALE'),('OTHER','OTHER')]
    dob = models.DateField(null=True,blank=True)
    gender = models.CharField(
        max_length=6,
        choices=genders
    )
    phone = models.CharField(max_length=10,null=True,blank=True)