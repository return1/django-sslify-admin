CHANGES
=======

v0.4.0 (2014-06-03)
-------------------

* add extra setting SSLIFY_ADMIN_DISABLE (thanks to jraez)

v0.3.0 (2014-02-06)
-------------------

* renamed SSLIFY_ADMIN_URL to SSLIFY_ADMIN_NAMESPACE
* added I18N support (thanks to Shahar Or)

v0.2.0 (2013-06-28)
-------------------

* only use django's is_secure() method to check for SECURE_PROXY_SSL_HEADER setting to disable header injection of HTTP_X_FORWARDED_PROTO (thanks to Bouke Haarsma)

v0.1.0 (2013-04-03)
-------------------

* Initial release.
