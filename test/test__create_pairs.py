__author__ = "Eppel, Tamas"
__copyright__ = "Copyright 2012"
__license__ = "BSD"

from lib.domain import _create_pairs

import unittest

class Test_create_pairs(unittest.TestCase):

    def testWrongNumberOfArgs(self):
        try:
            _create_pairs([1, 2, 3])
        except ValueError:
            return
        self.fail()

    def testCreatePairs(self):
        tuples = _create_pairs([1, 2, 3, 4])
        self.assertEquals([(1, 2), (3, 4)], tuples)
