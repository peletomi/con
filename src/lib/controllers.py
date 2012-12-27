from lib.service import ValueRepoService, InMemoryConfigLoader

import cherrypy

expose = cherrypy.expose

class RootController:

    def __init__(self, config):
        self.repo_service = ValueRepoService(InMemoryConfigLoader())

    @expose
    def get(self, directory, file, key, *context):
        return str(self.repo_service.get(directory, file, key, *context))