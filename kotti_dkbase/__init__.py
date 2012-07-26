from pyramid.httpexceptions import HTTPError
from pyramid.httpexceptions import HTTPNotFound
from kotti_dkbase.views import error_view
from kotti_dkbase.views import exception_decorator
import kotti.static as ks
from fanstatic import Resource, Library
from js.bootstrap import bootstrap_css

def setup_needed_group():
    """
    Modify the NeededGroups in kotti.static to not depend on
    bootstrap_responsive.
    """
    lib_kotti_new = Library("kotti2", ks.lib_kotti.path)
    for group in [ks.view_needed, ks.edit_needed]:
        for i, item in enumerate(group.resources):
            if item is ks.view_css:
                new_base = Resource(lib_kotti_new,
                                    "base.css",
                                    depends=[bootstrap_css, ],
                                    minified="base.min.css")
                group.resources[i] = Resource(lib_kotti_new,
                                              "view.css",
                                              depends=[new_base, ],
                                              minified="view.min.css")
            elif item is ks.edit_css:
                group.resources[i] = Resource(lib_kotti_new,
                                              "edit.css",
                                              depends=[bootstrap_css, ],
                                              minified="edit.min.css")

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
    setup_needed_group()