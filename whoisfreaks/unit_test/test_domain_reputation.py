import sys
import os

sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from icon_whoisfreaks.connection.connection import Connection
from icon_whoisfreaks.actions.domain_reputation import DomainReputation
import json
import logging


class TestDomainReputation(TestCase):
    def test_domain_reputation(self):
        """
        DO NOT USE PRODUCTION/SENSITIVE DATA FOR UNIT TESTS

        TODO: Implement test cases here
        """

        self.fail("Unimplemented Test Case")
