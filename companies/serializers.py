from rest_framework.serializers import ModelSerializer, SerializerMethodField

from companies.models import Address, Company


class AddressSerializer(ModelSerializer):
    class Meta:
        model = Address
        fields = [
            "id",
            "company",
            "contact_name",
            "value",
        ]


class CompanySerializer(ModelSerializer):
    addresses = AddressSerializer(many=True)
    trades = SerializerMethodField()
    covered_postcodes = SerializerMethodField()

    class Meta:
        model = Company
        fields = [
            "id",
            "name",
            "email",
            "phone_number",
            "addresses",
            "trades",
            "covered_postcodes",
        ]

    def get_trades(self, obj) -> list[str]:
        return obj.trades.values_list("trade", flat=True)

    def get_covered_postcodes(self, obj) -> list[str]:
        return obj.covered_postcodes.values_list("post_code", flat=True)
