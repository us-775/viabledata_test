# Generated by Django 4.1.7 on 2023-02-21 16:39

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Company",
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
                ("long_name", models.CharField(max_length=100)),
                ("short_name", models.CharField(blank=True, default="", max_length=50)),
                ("email", models.CharField(max_length=100)),
                ("phone_number", models.CharField(max_length=15)),
                (
                    "history",
                    models.TextField(
                        blank=True,
                        default="",
                        help_text="Information about the history of the company",
                        max_length=500,
                    ),
                ),
            ],
            options={
                "verbose_name_plural": "Companies",
            },
        ),
        migrations.CreateModel(
            name="TaxInfo",
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
                (
                    "type",
                    models.CharField(
                        choices=[
                            ("nino", "National Insurance number"),
                            ("ssn", "Social Security number"),
                        ],
                        max_length=4,
                    ),
                ),
                ("value", models.CharField(max_length=10)),
                (
                    "company",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="tax_infos",
                        to="companies.company",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="CoveredPostcode",
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
                ("post_code", models.CharField(max_length=7)),
                (
                    "company",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="covered_postcodes",
                        to="companies.company",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="CompanyTrade",
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
                ("trade", models.CharField(max_length=50)),
                ("note", models.TextField(blank=True, default="", max_length=500)),
                (
                    "level",
                    models.CharField(
                        choices=[("basic", "Basic"), ("advanced", "Advanced")],
                        help_text="The level to which the company holds the qualification for the trade",
                        max_length=8,
                    ),
                ),
                (
                    "company",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="trades",
                        to="companies.company",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="BankAccount",
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
                (
                    "type",
                    models.CharField(
                        choices=[("personal", "Personal"), ("business", "Business")],
                        max_length=8,
                    ),
                ),
                ("account_number", models.CharField(max_length=8)),
                ("sort_code", models.CharField(max_length=6)),
                (
                    "company",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="bank_accounts",
                        to="companies.company",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Address",
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
                (
                    "type",
                    models.CharField(
                        choices=[("office", "Office"), ("billing", "billing")],
                        default="office",
                        max_length=7,
                    ),
                ),
                (
                    "contact_name",
                    models.CharField(blank=True, default="", max_length=100),
                ),
                ("value", models.CharField(max_length=300)),
                (
                    "company",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="addresses",
                        to="companies.company",
                    ),
                ),
            ],
            options={
                "verbose_name_plural": "Addresses",
            },
        ),
    ]
