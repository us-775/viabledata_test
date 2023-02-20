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
    LEVEL_BASIC = "basic"
    LEVEL_ADVANCED = "advanced"
    LEVEL_CHOICES = [
        (LEVEL_BASIC, "Basic"),
        (LEVEL_ADVANCED, "Advanced"),
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
    TYPE_OFFICE = "office"
    TYPE_BILLING = "billing"
    TYPES = [
        (TYPE_OFFICE, "Office"),
        (TYPE_BILLING, "billing"),
    ]
    company = ForeignKey(Company, on_delete=models.CASCADE, related_name="addresses")
    type = CharField(max_length=7, choices=TYPES, default=TYPE_OFFICE)
    contact_name = CharField(max_length=100, blank=True, default="")
    value = CharField(max_length=300)

    class Meta:
        verbose_name_plural = "Addresses"


class TaxInfo(models.Model):
    TYPE_NINO = "nino"
    TYPE_SSN = "ssn"
    TYPES = [
        (TYPE_NINO, "National Insurance number"),
        (TYPE_SSN, "Social Security number"),
    ]

    company = ForeignKey(Company, on_delete=models.CASCADE, related_name="tax_infos")
    type = CharField(max_length=4, choices=TYPES)
    value = CharField(max_length=10)


class BankAccount(models.Model):
    TYPE_PERSONAL = "personal"
    TYPE_BUSINESS = "business"
    TYPES = [
        (TYPE_PERSONAL, "Personal"),
        (TYPE_BUSINESS, "Business"),
    ]

    company = ForeignKey(
        Company, on_delete=models.CASCADE, related_name="bank_accounts"
    )
    type = CharField(max_length=8, choices=TYPES)
    account_number = CharField(max_length=8)
    sort_code = CharField(max_length=6)


class CoveredPostcode(models.Model):
    company = ForeignKey(
        Company, on_delete=models.CASCADE, related_name="covered_postcodes"
    )
    post_code = CharField(max_length=7)
