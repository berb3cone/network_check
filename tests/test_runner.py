"""
#=============================================================#
# Purpose: from this file will be executed the existing tests #
#=============================================================#
"""

import unittest
from tests.nw_collection_tests import RemoveInvalidRecords


if __name__ == "__main__":
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()
    suite.addTest(loader.loadTestsFromTestCase(RemoveInvalidRecords))
    runner = unittest.TextTestRunner()
    runner.run(suite)
