from django.db import models
from authenticate.models import User
from .managers import SellerManager

# Create your models here.


class Seller(User):
    is_seller = True
    seller = SellerManager()

    class Meta:
        proxy = True


class SellerProfile(models.Model):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    org_name = models.CharField(max_length=200)
    org_info = models.TextField()
    org_email = models.CharField(max_length=200)
    org_address = models.TextField()
    org_contact = models.CharField(max_length=12)
    inventory_address = models.TextField()
    is_active = models.BooleanField(default=False)



