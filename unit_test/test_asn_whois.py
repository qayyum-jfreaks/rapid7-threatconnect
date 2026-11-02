import sys
import os

sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from komand_whoisfreaks.connection.connection import Connection
from komand_whoisfreaks.actions.asn_whois import AsnWhois
import json
import logging


class TestAsnWhois(TestCase):
    def test_asn_whois(self):
        """
        DO NOT USE PRODUCTION/SENSITIVE DATA FOR UNIT TESTS

        TODO: Implement test cases here
        """

        self.fail("Unimplemented Test Case")
