from django.urls import include, path
from rest_framework import routers

from companies.views import CompanyAddressViewSet, CompanyViewSet

companies_router = routers.SimpleRouter()
companies_router.register(r"companies", CompanyViewSet, basename="company")
addresses_router = routers.SimpleRouter()
addresses_router.register("", CompanyAddressViewSet, basename="company-addresses")

urlpatterns = companies_router.urls + [
    path("companies/<int:company_id>/addresses", include(addresses_router.urls)),
]
