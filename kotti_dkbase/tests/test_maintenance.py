def _setup():
    from wsgi_intercept.urllib2_intercept import install_opener
    install_opener()
    import wsgi_intercept
    from kotti_dkbase.maintenance import main

    settings = {
        'kotti_dkbase.maintenance_page':
        'kotti_dkbase:static/maintenance.html',
    }
    app = main({}, **settings)
    wsgi_intercept.add_wsgi_intercept('localhost', 5000, lambda: app)


def test_maintenance():
    _setup()
    import urllib2
    response = None
    try:
        response = urllib2.urlopen('http://localhost:5000/some_url/bla/bar')
    except urllib2.URLError, e:
        assert e.code == 503
        assert "Temporarily down for maintenance" in e.read()
    assert response is None
