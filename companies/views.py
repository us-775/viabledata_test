from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView

"""
 Company name
 Company abbreviation name (optional)

 Address
 Email
 Telephone number
 Trades (optional)
 Postcodes covered (optional)
 Company history (optional)

We should show to the public the following pieces of information: Company
abbreviation name if supplied, otherwise Company name; the Address; all the
Trades the company supplies; and the Company history."""


class CompanyView(APIView):
    def get(self, request, format=None):
        """ """
        squares = [i**2 for i in range(1, 11)]
        return Response(squares)
