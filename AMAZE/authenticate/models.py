from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.utils import timezone
from .managers import AmazeUserManager
from django.core.validators import RegexValidator

# Create your models here.


class User(AbstractBaseUser, PermissionsMixin):
    phone_regex = RegexValidator(
        regex=r"^(\+\d{1,2}\s?)?1?\-?\.?\s?\(?\d{3}\)?[\s.-]?\d{3}[\s.-]?\d{4}$",
        message="Phone number must be in correct format",
    )
    email = models.EmailField(unique=True)
    username = None
    user_name = models.CharField(max_length=100, blank=True, null=True)
    phone = models.CharField(validators=[phone_regex], max_length=20, unique=True)
    first_name = models.CharField(max_length=150, blank=True, null=True)
    last_name = models.CharField(max_length=150, blank=True, null=True)
    is_staff = models.BooleanField(default=False)
    is_seller = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(auto_now_add=True)

    object = AmazeUserManager()
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["user_name"]

    def __str__(self):
        if self.user_name:
            return self.user_name
        return self.email
