from rest_framework.viewsets import ModelViewSet

from companies.models import Address, Company
from companies.serializers import AddressSerializer, CompanySerializer


class CompanyViewSet(ModelViewSet):
    serializer_class = CompanySerializer
    queryset = Company.objects.all()


class CompanyAddressViewSet(ModelViewSet):
    serializer_class = AddressSerializer

    def get_queryset(self):
        return Address.objects.filter(company=self.kwargs["company_id"])
