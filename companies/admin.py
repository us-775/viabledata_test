from django.contrib import admin

from companies.models import (Address, BankAccount, Company, CompanyTrade,
                              CoveredPostcode, TaxInfo)

admin.site.register(Company)
admin.site.register(Address)
admin.site.register(TaxInfo)
admin.site.register(BankAccount)
admin.site.register(CompanyTrade)
admin.site.register(CoveredPostcode)
