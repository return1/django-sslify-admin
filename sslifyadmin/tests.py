from django.http import HttpResponsePermanentRedirect
from django.test import TestCase
from django.test.client import RequestFactory
from django.conf import settings

from sslifyadmin.middleware import SSLifyAdminMiddleware


class TestMiddlware(TestCase):
    def setUp(self):
        self.factory = RequestFactory()

    def test_admin_redirects_http_to_https(self):
        sslify_admin_url = getattr(settings, 'SSLIFY_ADMIN_URL', 'admin/')
        request = self.factory.get('/' + sslify_admin_url)
        self.assertTrue(request.build_absolute_uri().startswith('http://'))

        middleware = SSLifyAdminMiddleware()
        request = middleware.process_request(request)

        self.assertIsInstance(request, HttpResponsePermanentRedirect)
        self.assertTrue(request['Location'].startswith('https://'))

    def test_normal_request(self):
        request = self.factory.get('/foo/')
        self.assertTrue(request.build_absolute_uri().startswith('http://'))

        middleware = SSLifyAdminMiddleware()
        request = middleware.process_request(request)

        self.assertIsNone(request)


    def tearDown(self):
        del self.factory