from pyramid.httpexceptions import HTTPError
from pyramid.httpexceptions import HTTPNotFound
from kotti_dkbase.views import error_view
from kotti_dkbase.views import exception_decorator
from fanstatic import Library
from fanstatic import Resource
import kotti.static as ks


lib_dkbase = Library('kotti_dkbase', 'static')
view_css =  Resource(lib_dkbase, "layout.css", depends=[ks.view_css])
edit_css =  Resource(lib_dkbase, "edit.css", depends=[ks.edit_css])
nav_css =  Resource(lib_dkbase, "primary-navigation.css")


def add_fanstatic_resources(config):
    ks.view_needed.add(view_css)
    ks.view_needed.add(nav_css)
    ks.edit_needed.add(edit_css)


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
    add_fanstatic_resources(config)