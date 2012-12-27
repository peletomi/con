import lib.controllers

import cherrypy

from beaker.cache import CacheManager

DEFAULT_CONF_FILE = '~/.conrc'
DEFAULT_CACHE_ROOT = '/tmp/con-cache'

def setup_cache(config):
    cache_dir = (config['CACHE_ROOT'] if 'CACHE_ROOT' in config else DEFAULT_CACHE_ROOT)
    cache_opts = {'cache.type': 'file', 'cache.data_dir': '%s/data' % cache_dir, 'cache.lock_dir': '%s/lock' % cache_dir}
    cache_manager = CacheManager(**cache_opts)

def parse_args():
    from argparse import ArgumentParser

    parser = ArgumentParser(description='Configuration service')
    parser.add_argument('-c', '--config', help='Path to config file. (default: %s)' % DEFAULT_CONF_FILE, dest='config')
    parser.add_argument('-p', '--port', default=8080, help='Port number to listen on (default: 8080)')
    parser.add_argument('-b', '--bind', default='0.0.0.0', help='Bind IP')

    return parser.parse_args()

def main():

    setup_cache({})
    args = parse_args()

    cherrypy.config.update({'server.socket_host': args.bind, 'server.socket_port': int(args.port)})

    cherrypy.tree.mount(lib.controllers.RootController(None), '/')

    cherrypy.engine.start()
    cherrypy.engine.block()


if __name__ == '__main__':
    main()
