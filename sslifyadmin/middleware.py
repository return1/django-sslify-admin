from django.conf import settings
from django.http import HttpResponsePermanentRedirect
from django.core.urlresolvers import reverse


class SSLifyAdminMiddleware(object):
    """Force all admin requests to use HTTPs. If we get an HTTP request, we'll just
    force a redirect to HTTPs.

    .. note::
        This will only take effect if ``settings.DEBUG`` is False.
    """

    def process_request(self, request):
        sslify_admin_namespace = getattr(settings, 'SSLIFY_ADMIN_NAMESPACE', 'admin')
        sslify_admin_disable = getattr(settings, 'SSLIFY_ADMIN_DISABLE', settings.DEBUG)
        if request.path.startswith(reverse('%s:index' % sslify_admin_namespace)) and \
                not (sslify_admin_disable or request.is_secure()):
            url = request.build_absolute_uri(request.get_full_path())
            secure_url = url.replace('http://', 'https://')
            return HttpResponsePermanentRedirect(secure_url)
