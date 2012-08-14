from pyramid.httpexceptions import HTTPInternalServerError
from pyramid_mailer.message import Message
from kotti.message import get_mailer
from kotti import get_settings


def mail_admin(msg):
    """
    Send given message to the admins.
    """
    admin = get_settings().get('kotti_dkbase.admin_email')
    message = Message(
        recipients=[admin],
        subject=u'Server-Error',
        body=msg,
    )
    mailer = get_mailer()
    mailer.send_immediately(message)


def exception_decorator(view):
    """
    Transform generic exceptions to Error 500
    """
    def f(exception, request):
        return view(HTTPInternalServerError(str(exception)), request)
    return f


def error_view(exception, request):
    should_mail = get_settings().get('kotti_dkbase.send_error_mails') == "True"
    if should_mail and exception.code != 404:
        mail_admin(str(exception) + str(request))
    request.response.status_int = exception.code
    return {}
