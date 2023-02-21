from django.db import models
from drf_spectacular.utils import (OpenApiExample, OpenApiParameter,
                                   extend_schema)
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

    def get_queryset(self):
        """
        Supports filtering on `trade`, `postcode` and `level`.
        See documentation for the `GET /companies/` endpoint for more info.
        """
        queryset = Company.objects.all()
        trade_filter_query = self.request.query_params.getlist("trade")
        if trade_filter_query:
            queryset = queryset.filter(trades__trade__in=trade_filter_query)

        postcode_filter_query = self.request.query_params.getlist("postcode")
        if postcode_filter_query:
            queryset = queryset.filter(
                covered_postcodes__post_code__in=postcode_filter_query
            )

        # '?level=basic' or '?level=advanced'
        level_filter_query = self.request.query_params.get("level")
        if level_filter_query:
            queryset = queryset.filter(trades__level=level_filter_query)

        return queryset.distinct()

    @extend_schema(
        parameters=[
            OpenApiParameter(
                name="trade",
                description="Filter by trade",
                many=True,
            ),
            OpenApiParameter(
                name="postcode",
                description="Filter by postcode",
                many=True,
            ),
            OpenApiParameter(
                name="level",
                description="Filter by level of qualifications the company has (in any trade)",
                examples=[
                    OpenApiExample("none", summary="-", value=""),
                    OpenApiExample("basic", summary="Basic", value="basic"),
                    OpenApiExample("advanced", summary="Advanced", value="advanced"),
                ],
            ),
        ],
        description="The client can search companies by passing in URL query parameters `trade`, `postcode` and/or `level`. For example, `/companies/?postcode=SE12AA&postcode=E13TP&trade=plumbing` will show companies that cover either 'SE12AA' or 'E13TP', and are also in the 'plumbing' trade. Another example: `/companies/?level=advanced` will show companies that have at least one trade for which they have advanced qualifaction.",
    )
    def list(self, request, *args, **kwargs):
        """hello how  ru"""
        return super().list(request, *args, **kwargs)

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
