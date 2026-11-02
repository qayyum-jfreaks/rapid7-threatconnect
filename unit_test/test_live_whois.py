import sys
import os

sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from komand_whoisfreaks.connection.connection import Connection
from komand_whoisfreaks.actions.live_whois import LiveWhois
import json
import logging


class TestLiveWhois(TestCase):
    def test_live_whois(self):
        """
        DO NOT USE PRODUCTION/SENSITIVE DATA FOR UNIT TESTS

        TODO: Implement test cases here
        """

        self.fail("Unimplemented Test Case")
