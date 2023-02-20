from django.db import models
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.serializers import Serializer
from rest_framework.viewsets import ModelViewSet

from companies.models import (Address, BankAccount, Company, CompanyTrade,
                              TaxInfo)
from companies.serializers import (AddressSerializer, BankAccountSerializer,
                                   CompanySerializer, CompanyTradeSerializer,
                                   TaxInfoSerializer)


class CompanyViewSet(ModelViewSet):
    serializer_class = CompanySerializer
    queryset = Company.objects.all()

    @staticmethod
    def _deserialize_related_objects(
        model_cls: models.Model, serializer_cls: Serializer, company_id: int
    ) -> Response:
        """
        Helper method
        """
        objects = model_cls.objects.filter(company=company_id)
        serializer = serializer_cls(objects, many=True)
        return Response(serializer.data)

    @action(methods=["get"], detail=True)
    def address(self, request, pk, *args, **kwargs):
        return self._deserialize_related_objects(Address, AddressSerializer, pk)

    @action(methods=["get"], detail=True)
    def tax_info(self, request, pk, *args, **kwargs):
        return self._deserialize_related_objects(TaxInfo, TaxInfoSerializer, pk)

    @action(methods=["get"], detail=True)
    def trades(self, request, pk, *args, **kwargs):
        return self._deserialize_related_objects(
            CompanyTrade, CompanyTradeSerializer, pk
        )

    @action(methods=["get"], detail=True)
    def bank_accounts(self, request, pk, *args, **kwargs):
        return self._deserialize_related_objects(BankAccount, BankAccountSerializer, pk)
