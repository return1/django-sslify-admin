from os.path import abspath, dirname, join, normpath

from setuptools import setup

from sslifyadmin import __version__


setup(

    # Basic package information:
    name='django-sslify-admin',
    version=__version__,
    packages=('sslifyadmin',),

    # Packaging options:
    zip_safe=False,
    include_package_data=True,

    # Package dependencies:
    install_requires=['Django>=1.2'],

    # Metadata for PyPI:
    author='Dominique Lederer',
    author_email='dominique.lederer@return1.at',
    license='mit',
    url='https://github.com/return1/django-sslify-admin',
    keywords='django ssl https middleware admin',
    description='Force SSL on your Django admin site.',
    long_description=open(normpath(join(dirname(abspath(__file__)),
                                        'README.rst'))).read(),
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Topic :: Internet :: WWW/HTTP :: WSGI :: Middleware',
        'Topic :: Software Development :: Libraries :: Python Modules',
        "Framework :: Django",
    ],

    tests_require=(
        'django',
    ),
    test_suite='runtests.runtests',

)
