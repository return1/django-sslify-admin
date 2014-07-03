from os.path import abspath, dirname, join, normpath

from setuptools import setup


setup(

    # Basic package information:
    name='django-sslify-admin',
    version='0.4',
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
                                        'README.md'))).read(),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.4",
        "Programming Language :: Python :: 2.5",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
        "Framework :: Django",
    ],

    tests_require = (
        'django',
    ),
    test_suite='runtests.runtests',

)
