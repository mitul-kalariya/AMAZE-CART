from django.contrib.auth.models import BaseUserManager


class AmazeUserManager(BaseUserManager):
    def create_user(
        self,
        email,
        phone,
        user_name,
        password,
        **other_fields,
    ):
        if not email:
            raise ValueError("You must Provide an email address")
        if not phone:
            raise ValueError("A user must provide a phone number for account")
        email = self.normalize_email(email)
        user = self.model(email=email, phone=phone, user_name=user_name, **other_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(
        self,
        email,
        user_name,
        password,
        **other_fields,
    ):
        admin_contact = "+000000000"
        other_fields.setdefault("is_superuser", True)
        other_fields.setdefault("is_staff", True)
        other_fields.setdefault("is_active", True)
        if other_fields.get("is_staff") is not True:
            raise ValueError("Superuser must be assigned to is_staff=True")
        if other_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must be assigned to is_superuser=True")

        return self.create_user(
            email, user_name, admin_contact, password, **other_fields
        )

    # def create_seller(
    #     self,
    #     email,
    #     phone,
    #     user_name,
    #     password,
    #     **other_fields,
    # ):
    #     other_fields.setdefault("is_seller", True)
    #     if other_fields.get("is_seller") is not True:
    #         raise ValueError("A seller must be assigned is_seller=True")
    #     if not phone:
    #         raise ValueError("A seller must add a phone number to add his/her account")
    #     return self.create_user(email, phone, user_name, password, **other_fields)
