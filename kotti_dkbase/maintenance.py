"""
Provides a maintenance WSGI app to be used with Paste Deploy.

[app:maintenance]
use = egg:kotti_dkbase
kotti_dkbase.maintenance_page = my_package:static/maintenance.html
"""

from pyramid.path import AssetResolver


def main(global_config, **settings):
    """ This function is a 'paste.app_factory' and returns a WSGI
    application.
    """
    static = AssetResolver().resolve(settings['kotti_dkbase.maintenance_page'])
    with open(static.abspath(), 'r') as f:
        body = '\n'.join(f.readlines())

    def maintenance(environ, start_response):
        start_response('503 Service Unavailable',
                       [('content-type', 'text/html')])
        return [body]

    return maintenance
