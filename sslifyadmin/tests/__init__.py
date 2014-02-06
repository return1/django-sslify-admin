from django.http import HttpResponsePermanentRedirect
from django.test import TestCase
from django.test.client import RequestFactory
from django.conf import settings
from django.utils import translation
from django.core.urlresolvers import reverse, clear_url_caches
from django.test.utils import override_settings

from sslifyadmin.middleware import SSLifyAdminMiddleware


class TestMiddlware(TestCase):
    urls = 'sslifyadmin.tests.urls_admin'

    def setUp(self):
        self.factory = RequestFactory()


    def tearDown(self):
        del self.factory


    def test_admin_redirects_http_to_https(self):
        request = self.factory.get('/admin_custom_namespace/')
        self.assertTrue(request.build_absolute_uri().startswith('http://'))

        middleware = SSLifyAdminMiddleware()
        request = middleware.process_request(request)

        self.assertIsInstance(request, HttpResponsePermanentRedirect)
        self.assertTrue(request['Location'].startswith('https://'))

    @override_settings(ROOT_URLCONF='sslifyadmin.tests.urls_admin_i18n')
    def test_i18n_admin_redirects_http_to_https(self):
        with translation.override('en'):
            request = self.factory.get('/en/admin_custom_namespace/')
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