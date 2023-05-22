# Generated by Django 4.1.7 on 2023-05-22 11:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.db.models.manager


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("authenticate", "0002_user_is_active"),
    ]

    operations = [
        migrations.CreateModel(
            name="Seller",
            fields=[],
            options={
                "proxy": True,
                "indexes": [],
                "constraints": [],
            },
            bases=("authenticate.user",),
            managers=[
                ("seller", django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name="SellerProfile",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("org_name", models.CharField(max_length=200)),
                ("org_info", models.TextField()),
                ("org_email", models.CharField(max_length=200)),
                ("org_address", models.TextField()),
                ("org_contact", models.CharField(max_length=12)),
                ("inventory_address", models.TextField()),
                ("is_active", models.BooleanField(default=False)),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
