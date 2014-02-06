#!/usr/bin/env python

import os, sys

from django.conf import settings


if not settings.configured:
    settings.configure(
        INSTALLED_APPS=['sslifyadmin'],
        ROOT_URLCONF='urls',
        DATABASES={"default": {"ENGINE": "django.db.backends.sqlite3"}},
    )


def runtests(*test_args):
    if not test_args:
        test_args = ["sslifyadmin"]

    parent = os.path.dirname(os.path.abspath(__file__))
    sys.path.insert(0, parent)

    try:
        from django.test.simple import DjangoTestSuiteRunner

        def run_tests(test_args, verbosity, interactive):
            runner = DjangoTestSuiteRunner(
                verbosity=verbosity, interactive=interactive, failfast=False)
            return runner.run_tests(test_args)
    except ImportError:
        # for Django versions that don't have DjangoTestSuiteRunner
        from django.test.simple import run_tests
    failures = run_tests(test_args, verbosity=1, interactive=True)
    sys.exit(failures)


if __name__ == '__main__':
    runtests()