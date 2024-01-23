# pylint: skip-file
import unittest
from testing_imports import *
from HTMLTestRunner import HTMLTestRunner

class PublicTests(unittest.TestCase):

    def test_public_ex1(self):
        self.assertTrue(decompress_file('./data/TMDB.zip', './data'))
        self.assertFalse(decompress_file('./data/madeUpZip.zip', './data'))



if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(PublicTests))
    runner = HTMLTestRunner(log=True, verbosity=2, output="reports", title="PAC4")
    runner.run(suite)