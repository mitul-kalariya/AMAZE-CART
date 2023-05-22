from django.contrib.auth.models import BaseUserManager
from django.db.models.query import QuerySet


class SellerManager(BaseUserManager):
    def get_queryset(self, *args, **kwargs) -> QuerySet:
        result = super().get_queryset(*args, **kwargs)
        return result.filter(is_seller=True)
