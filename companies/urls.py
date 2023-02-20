from rest_framework import routers

from companies.views import CompanyViewSet

companies_router = routers.SimpleRouter()
companies_router.register(r"companies", CompanyViewSet, basename="company")
urlpatterns = companies_router.urls
