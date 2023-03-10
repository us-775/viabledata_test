from django.test import TestCase

from companies.models import (Address, BankAccount, Company, CompanyTrade,
                              CoveredPostcode, TaxInfo)


class CompanyTestCase(TestCase):
    LIST_URL = "/companies/"
    DETAIL_URL = "/companies/1/"

    EXPECTED_COMPANY_RESPONSE = {
        "id": 1,
        "name": "BP",  # abbreviated name is displayed, not the long name
        "email": "sample@text.com",
        "phone_number": "02134567890",
        "history": "Formed in 1560",
        "addresses": [
            {
                "company": 1,
                "contact_name": "Person Surname",
                "id": 1,
                "value": "1 Oil Street",
            },
            {
                "company": 1,
                "contact_name": "",
                "id": 2,
                "value": "24 Road Avenue",
            },
        ],
        "covered_postcodes": ["SW11 2AA"],
        "trades": ["oil extraction", "oil refining"],
        "bank_accounts": [
            {
                "account_number": "12345678",
                "company": 1,
                "id": 1,
                "sort_code": "123456",
                "type": "business",
            }
        ],
        "tax_infos": [{"company": 1, "id": 1, "type": "ssn", "value": "AAAGGSSSS"}],
    }

    @classmethod
    def setUpTestData(cls):
        """
        Company 1 (British Petroleum)
        - 2 addresses
        - 1 covered postcode
        - 2 trades
        - 1 bank account
        - 1 tax info
        """
        # Company 1
        company_1 = Company(
            id=1,
            long_name="British Petroleum",
            short_name="BP",
            email="sample@text.com",
            phone_number="02134567890",
            history="Formed in 1560",
        )
        company_1.save()

        address1 = Address(
            company=company_1, contact_name="Person Surname", value="1 Oil Street"
        )
        address1.save()
        address2 = Address(
            company=company_1, type=Address.TYPE_BILLING, value="24 Road Avenue"
        )
        address2.save()

        covered_postcode1 = CoveredPostcode(company=company_1, post_code="SW11 2AA")
        covered_postcode1.save()

        trade1 = CompanyTrade(
            company=company_1,
            trade="oil extraction",
            note="don't spill anything into the sea",
            level=CompanyTrade.LEVEL_BASIC,
        )
        trade1.save()
        trade2 = CompanyTrade(
            company=company_1, trade="oil refining", level=CompanyTrade.LEVEL_ADVANCED
        )
        trade2.save()

        bank_account = BankAccount(
            company=company_1,
            type=BankAccount.TYPE_BUSINESS,
            account_number="12345678",
            sort_code="123456",
        )
        bank_account.save()

        tax_info = TaxInfo(company=company_1, type=TaxInfo.TYPE_SSN, value="AAAGGSSSS")
        tax_info.save()

    def test_list(self):
        response = self.client.get(self.LIST_URL)
        assert response.status_code == 200
        expected_data = [self.EXPECTED_COMPANY_RESPONSE]

        actual_data = response.json()
        assert actual_data == expected_data

    def test_get(self):
        response = self.client.get(self.DETAIL_URL)
        assert response.status_code == 200
        expected_data = self.EXPECTED_COMPANY_RESPONSE

        actual_data = response.json()
        assert actual_data == expected_data

    def test_partial_update(self):
        """
        Update the email address and history
        """
        payload = {"email": "new_email_address@gmail.com", "history": "Formed in 1950"}
        response = self.client.patch(
            self.DETAIL_URL, data=payload, content_type="application/json"
        )
        assert response.status_code == 200
        expected_data = (
            self.EXPECTED_COMPANY_RESPONSE
        )  # everything else should be the same
        expected_data["email"] = "new_email_address@gmail.com"
        expected_data["history"] = "Formed in 1950"
        actual_data = response.json()
        assert actual_data == expected_data
