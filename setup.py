import os
from setuptools import setup

with open(os.path.join(os.path.dirname(__file__), 'README.rst')) as readme:
    README = readme.read()

setup(
    name='django-search-admin-autcomplete',
    version='0.1',
    packages=[
        'search_admin_autocomplete',
    ],
    url='https://github.com/linevich/django-search-admin-autocomplete',
    license='MIT',
    long_description=README,
    author='linevich',
    author_email='mail@linevich.net',
    description='Simple django app that add autocomplete to search inside admin panel.',
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
)
