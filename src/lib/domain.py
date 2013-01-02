__author__ = "Eppel, Tamas"
__copyright__ = "Copyright 2012"
__license__ = "BSD"

def _create_pairs(args):
    result = []

    if args is None or args == []:
        return result

    if len(args) % 2 != 0:
        raise ValueError('args length is not even. args [%s]' % str(args))

    i = 0
    while i < len(args):
        k = args[i]
        v = args[i + 1]
        result.append((k, v))
        i += 2
    return result

class Key():

    def __init__(self, key, context=[]):
        self.key = key
        self.context = context
        self.repo_keys = [self]
        if context:
            self._addContext(context)

            c = context
            while True:
                c = c[0:-2]
                self.repo_keys.append(Key(key, c))
                if not c:
                    break


    def _addContext(self, context):
        self.context = set()
        pairs = _create_pairs(context)
        for t in pairs:
            self.context.add(t)

        self.context_keys = map(lambda p: p[0], pairs)

    def __eq__(self, other):
        return self.key == other.key and self.context == other.context

    def __hash__(self):
        hash = 17
        if self.context:
            for t in self.context:
                hash += t.__hash__()
        hash += self.key.__hash__()
        return 31 * hash

    def __str__(self):
        return '%s [%s]' % (self.key, ', '.join(self.context))

class ValueRepo():

    def __init__(self):
        self.values = {}

    def __setitem__(self, key, value):
        if not isinstance(key, Key):
            raise TypeError('has to be of the Key')
        self.values[key] = value

    def __getitem__(self, key):
        if not isinstance(key, Key):
            raise TypeError('has to be of the Key')

        for k in key.repo_keys:
            if k in self.values:
                return self.values[k]

