import sys
import os

sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from icon_whoisfreaks.connection.connection import Connection
from icon_whoisfreaks.actions.bulk_whois import BulkWhois
import json
import logging


class TestBulkWhois(TestCase):
    def test_bulk_whois(self):
        """
        DO NOT USE PRODUCTION/SENSITIVE DATA FOR UNIT TESTS

        TODO: Implement test cases here
        """

        self.fail("Unimplemented Test Case")
