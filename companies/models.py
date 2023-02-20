from django.db import models
from django.db.models import CharField, ForeignKey, TextField


class Company(models.Model):
    long_name = CharField(max_length=100)
    short_name = CharField(max_length=50, blank=True, default="")
    email = CharField(max_length=100)
    phone_number = CharField(max_length=15)

    def __str__(self):
        return f"{self.name} (id {self.id})"

    class Meta:
        verbose_name_plural = "Companies"

    @property
    def name(self):
        return self.short_name or self.long_name


class CompanyTrade(models.Model):
    LEVEL_CHOICES = [
        ("basic", "Basic"),
        ("advanced", "Advanced"),
    ]

    company = ForeignKey(Company, on_delete=models.CASCADE, related_name="trades")
    trade = CharField(max_length=50)
    note = TextField(max_length=500, blank=True, default="")
    level = CharField(
        max_length=8,
        choices=LEVEL_CHOICES,
        help_text="The level to which the company holds the qualification for the trade",
    )


class Address(models.Model):
    ADDRESS_TYPES = [
        ("office", "Office"),
        ("billing", "billing"),
    ]
    company = ForeignKey(Company, on_delete=models.CASCADE, related_name="addresses")
    contact_name = CharField(max_length=100, blank=True, default="")
    value = CharField(max_length=300)

    class Meta:
        verbose_name_plural = "Addresses"


class TaxInfo(models.Model):
    TYPES = [
        ("nino", "National Insurance number"),
        ("ssn", "Social Security number"),
    ]

    company = ForeignKey(Company, on_delete=models.CASCADE, related_name="tax_infos")
    type = CharField(max_length=4, choices=TYPES)
    value = CharField(max_length=10)


class BankAccount(models.Model):
    TYPES = [
        ("personal", "Personal"),
        ("business", "Business"),
    ]

    company = ForeignKey(
        Company, on_delete=models.CASCADE, related_name="bank_accounts"
    )
    account_number = CharField(max_length=8)
    sort_code = CharField(max_length=6)


class CoveredPostcode(models.Model):
    company = ForeignKey(
        Company, on_delete=models.CASCADE, related_name="covered_postcodes"
    )
    post_code = CharField(max_length=7)
