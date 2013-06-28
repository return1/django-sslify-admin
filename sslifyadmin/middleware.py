from django.conf import settings
from django.http import HttpResponsePermanentRedirect


class SSLifyAdminMiddleware(object):
    """Force all admin requests to use HTTPs. If we get an HTTP request, we'll just
    force a redirect to HTTPs.

    .. note::
        This will only take effect if ``settings.DEBUG`` is False.
    """

    def process_request(self, request):
        sslify_admin_url = getattr(settings, 'SSLIFY_ADMIN_URL', 'admin/')
        if request.path.startswith('/' + sslify_admin_url) and \
                not (settings.DEBUG or request.is_secure()):
            url = request.build_absolute_uri(request.get_full_path())
            secure_url = url.replace('http://', 'https://')
            return HttpResponsePermanentRedirect(secure_url)
