# django-sslify-admin

Force SSL on your Django admin site


## Install

To install ``django-sslify-admin``, simply run ``pip install django-sslify-admin`` and
you'll get the latest version installed automatically.


## Usage

Modify your Django ``settings.py`` file, and prepend
``sslifyadmin.middleware.SSLifyAdminMiddleware`` to your ``MIDDLEWARE_CLASSES`` setting:

``` python
MIDDLEWARE_CLASSES = (
    'sslifyadmin.middleware.SSLifyAdminMiddleware',
    # ...
)
```

**NOTE**: Make sure ``sslify.middleware.SSLifyMiddleware`` is the first
middleware class listed, as this will ensure that if a user makes an unsecure
request (over HTTP), they will be redirected to HTTPs before any actual
processing happens.

### Custom admin url?
If you are using a custom admin url, you have to set ``SSLIFY_ADMIN_URL`` in your ``settings.py``:

``` python
# SSLIFY_ADMIN_URL = "admin/" # default
SSLIFY_ADMIN_URL = "myadminurl/" # custom
```

### Behind a Proxy? (Heroku)

If your Django app is behind a proxy (like Heroku), though, the proxy may be “swallowing” the fact that a request is HTTPS, using a non-HTTPS
connection between the proxy and Django.

In this situation, you’ll want to configure the proxy (Heroku already does that for you) to set a custom HTTP header that tells Django whether
the request came in via HTTPS, and you’ll want to set ``SECURE_PROXY_SSL_HEADER`` so that Django knows what header to look for, like this:

``` python
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
```


## Notes

This code was taken and modified from [this StackOverflow
thread](http://stackoverflow.com/questions/8436666/how-to-make-python-on-heroku-https-only).
This Project is also influenced by Randall Degges [django-sslify](https://github.com/rdegges/django-sslify), use this, if you want to secure your
whole site, and not only the admin interface of Django.


## Tests

``` bash
$ git clone https://github.com/return1/django-sslify-admin.git
$ cd django-sslify-admin
$ python setup.py develop
...
$ python setup.py test
Creating test database for alias 'default'...
..
----------------------------------------------------------------------
Ran 2 tests in 0.003s

OK
Destroying test database for alias 'default'...
```



# License

[http://return1.mit-license.org/](http://return1.mit-license.org/)