from pyramid.httpexceptions import HTTPError
from pyramid.httpexceptions import HTTPNotFound
from kotti_dkbase.views import error_view
from kotti_dkbase.views import exception_decorator

def includeme(config):
    config.include('pyramid_zcml')
    config.load_zcml('configure.zcml')
    config.add_view(
        error_view,
        context=HTTPNotFound,
        renderer='kotti_dkbase:templates/view/error-404.pt',
        )
    config.add_view(
        error_view,
        context=HTTPError,
        renderer='kotti_dkbase:templates/view/error.pt',
        )
    config.add_view(
        error_view,
        decorator=exception_decorator,
        context=Exception,
        renderer='kotti_dkbase:templates/view/error.pt',
        )
    config.add_static_view('static-kotti_dkbase', 'kotti_dkbase:static')
    config.override_asset('kotti', 'kotti_dkbase:kotti-overrides/')