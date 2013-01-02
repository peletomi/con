
from lib.domain import ValueRepo, Key

from yaml import load, dump
try:
    from yaml import CLoader as Loader
except ImportError:
    from yaml import Loader

import os.path

class YamlConfigLoader():

    def __init__(self, config):
        self.config = config

    def load_config(self, directory, file):
        repo = ValueRepo()
        file_name = os.path.join(self.config['repository_path'], directory, file + '.yaml')
        with open(file_name) as f:
            data = load(f, Loader=Loader) # FIXME handle file not exists
            for d in data:
                for k, v in d.iteritems():
                    value = None # FIXME no value specified
                    context = []
                    for kv, vv in v.iteritems():
                        if kv == 'value':
                            value = vv
                        else:
                            context.append(kv)
                            context.append(str(vv))
                    repo[Key(k, context=context)] = value
        return repo

class InMemoryConfigLoader():

    def __init__(self, config):
        self.config = config

    def load_config(self, directory, file):
        repo = ValueRepo()
        repo[Key('foo.bar')] = 1
        return repo

class ValueRepoService:

    def __init__(self, loader):
        self.loader = loader

    def get(self, directory, file, key, *context):
        return self.loader.load_config(directory, file)[Key(key, context=list(context))]
