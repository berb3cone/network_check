import unittest
from tests.utils import *


class RemoveInvalidRecords(unittest.TestCase):

    def test_remove_from_network1(self):
        res, msg = verify_method("network1", "remove_invalid_records")
        self.assertTrue(res, msg=msg)

    def test_remove_from_network2(self):
        res, msg = verify_method("network2", "remove_invalid_records")
        self.assertTrue(res, msg=msg)

    def test_sort_in_network3(self):
        res, msg = verify_method("network3", "sort_records")
        self.assertTrue(res, msg=msg)

    def test_sort_in_network4(self):
        res, msg = verify_method("network4", "sort_records")
        self.assertTrue(res, msg=msg)
