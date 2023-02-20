from django.test import TestCase


class FooTestCase(TestCase):
    def test_base(self):
        assert 3 == 3
