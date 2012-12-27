from lib.domain import _create_pairs

import unittest

class CreatePairsTest(unittest.TestCase):

    def testWrongNumberOfArgs(self):
        try:
            _create_pairs([1, 2, 3])
        except ValueError:
            return
        self.fail()

    def testCreatePairs(self):
        tuples = _create_pairs([1, 2, 3, 4])
        self.assertEquals([(1, 2), (3, 4)], tuples)
