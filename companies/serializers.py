from rest_framework.serializers import ModelSerializer, SerializerMethodField

from companies.models import (Address, BankAccount, Company, CompanyTrade,
                              TaxInfo)


class AddressSerializer(ModelSerializer):
    class Meta:
        model = Address
        fields = [
            "id",
            "company",
            "contact_name",
            "value",
        ]


class BankAccountSerializer(ModelSerializer):
    class Meta:
        model = BankAccount
        fields = [
            "id",
            "company",
            "type",
            "account_number",
            "sort_code",
        ]


class TaxInfoSerializer(ModelSerializer):
    class Meta:
        model = TaxInfo
        fields = [
            "id",
            "company",
            "type",
            "value",
        ]


class CompanyTradeSerializer(ModelSerializer):
    class Meta:
        model = CompanyTrade
        fields = [
            "id",
            "company",
            "trade",
            "note",
            "level",
        ]


class CompanySerializer(ModelSerializer):
    addresses = AddressSerializer(many=True)
    trades = SerializerMethodField()
    covered_postcodes = SerializerMethodField()
    bank_accounts = BankAccountSerializer(many=True)
    tax_infos = TaxInfoSerializer(many=True)

    class Meta:
        model = Company
        fields = [
            "id",
            "name",
            "email",
            "phone_number",
            "history",
            "addresses",
            "trades",
            "covered_postcodes",
            "bank_accounts",
            "tax_infos",
        ]

    def get_trades(self, obj) -> list[str]:
        """
        Summary of trades
        """
        return obj.trades.values_list("trade", flat=True)

    def get_covered_postcodes(self, obj) -> list[str]:
        """
        Summary of postcodes covered
        """
        return obj.covered_postcodes.values_list("post_code", flat=True)
