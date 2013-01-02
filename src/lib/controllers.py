from lib.service import ValueRepoService, InMemoryConfigLoader, YamlConfigLoader

import cherrypy

expose = cherrypy.expose

class RootController:

    def __init__(self, config):
        self.config = config
        self.repo_service = ValueRepoService(YamlConfigLoader(config))

    @expose
    def get(self, directory, file, key, *context):
        return str(self.repo_service.get(directory, file, key, *context))