import sys
import os

sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from icon_whoisfreaks.connection.connection import Connection
from icon_whoisfreaks.actions.reverse_dns import ReverseDns
import json
import logging


class TestReverseDns(TestCase):
    def test_reverse_dns(self):
        """
        DO NOT USE PRODUCTION/SENSITIVE DATA FOR UNIT TESTS

        TODO: Implement test cases here
        """

        self.fail("Unimplemented Test Case")
