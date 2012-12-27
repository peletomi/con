
from lib.domain import Key

import unittest

class KeyTest(unittest.TestCase):

    def testEq(self):
        key1 = Key('foo')
        key2 = Key('foo')

        self.assertEquals(key1, key2)

    def testEqWithContext(self):
        key2 = Key('foo', ['quux', 1])
        key1 = Key('foo', ['quux', 1])

        self.assertEquals(key1, key2)

    def testNotEq(self):
        key1 = Key('foo')
        key2 = Key('bar')

        self.assertNotEquals(key1, key2)

    def testNotEqWithContext(self):
        key1 = Key('foo', ['quux', 1])
        key2 = Key('foo', ['quux', 2])

        self.assertNotEquals(key1, key2)

    def testKeySimple(self):
        key = Key('foo')
        self.assertEquals('foo', key.key)

    def testKeyContext(self):
        key = Key('foo', ['quux', 1])
        self.assertEquals({('quux', 1)}, key.context)

    def testKeyMoreContext(self):
        key = Key('foo', ['quux', 1, 'bar', 'baz'])
        self.assertEquals({('quux', 1), ('bar', 'baz')}, key.context)
