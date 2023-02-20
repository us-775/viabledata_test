from django.urls import path
from rest_framework import routers

from companies.views import CompanyView

router = routers.SimpleRouter()
api_urlpatterns = [
    path("", CompanyView.as_view()),
]

urlpatterns = router.urls + api_urlpatterns
