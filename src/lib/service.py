
from lib.domain import ValueRepo, Key

class InMemoryConfigLoader():

    def load_config(self, directory, file):
        repo = ValueRepo()
        repo[Key('foo.bar')] = 1
        return repo

class ValueRepoService:

    def __init__(self, loader):
        self.loader = loader

    def get(self, directory, file, key, *context):
        return self.loader.load_config(directory, file)[Key(key, list(context))]
