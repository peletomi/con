
from lib.domain import ValueRepo, Key

import unittest

class ValueRepoTest(unittest.TestCase):

    def setUp(self):
        self.repo = ValueRepo()

    def testAddGetSimple(self):
        """Exact match between repo and retrieval key."""
        self.repo[Key('foo')] = 'bar'

        v = self.repo[Key('foo')]
        self.assertEqual('bar', v)

        self.assertIsNone(self.repo[Key('xxx')])

    def testAddGetWithFallback(self):
        """A key with context is retrieved, but the repo has a more general key.
        In this case this should be retrieved."""
        self.repo[Key('foo')] = 'bar'

        v = self.repo[Key('foo', ['quux', 1])]
        self.assertEqual('bar', v)

    def testAddWithContext(self):
        """Repo and retrieval keys have the same context and there is a general key as well.
        In this case the exact match should be retrieved."""
        self.repo[Key('foo')] = 'baz'
        self.repo[Key('foo', ['quux', 1])] = 'bar'

        v = self.repo[Key('foo', ['quux', 1])]
        self.assertEqual('bar', v)

    def testAddWithMoreContexts(self):
        """Repo and retrieval keys have contexts, but the retrieval key not so specific."""
        repo_key1 = Key('foo')
        repo_key2 = Key('foo', ['quux', 1])
        repo_key3 = Key('foo', ['quux', 1, 'bar', 'baz'])

        retrieval_key = Key('foo', ['quux', 1])

        self.repo[repo_key1] = 1
        self.repo[repo_key2] = 2
        self.repo[repo_key3] = 3

        v = self.repo[retrieval_key]
        self.assertEqual(2, v)

    def testRepoContextOrderDoesNotMatter(self):
        repo_key1 = Key('foo')
        repo_key2 = Key('foo', ['bar', 'baz', 'quux', 1])

        retrieval_key = Key('foo', ['quux', 1, 'bar', 'baz'])

        self.repo[repo_key1] = 1
        self.repo[repo_key2] = 2

        v = self.repo[retrieval_key]
        self.assertEqual(2, v)

    def testRepoContextOnlyLessSpecific(self):
        repo_key1 = Key('foo')
        repo_key2 = Key('foo', ['quux', 1])
        repo_key3 = Key('foo', ['bar', 'baz'])

        retrieval_key = Key('foo', ['quux', 1, 'bar', 'baz'])

        self.repo[repo_key1] = 1
        self.repo[repo_key2] = 2
        self.repo[repo_key3] = 3

        v = self.repo[retrieval_key]
        self.assertEqual(2, v)