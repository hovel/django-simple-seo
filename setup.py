import os

from setuptools import setup

setup(
    name='Django SimpleSEO',
    version='0.0.1',
    author='Glamping Hub',
    author_email='it@glampinghub.com',
    packages=['simpleseo'],
    url='https://github.com/Glamping-Hub/django-simple-seo',
    license='LICENSE',
    description='Simple SEO app for django framework',
    long_description=open(os.path.join(os.path.dirname(__file__), 'README.md')).read(),
    requires=[
        'Django (>=1.11.0)',
    ],
    include_package_data=True,
    zip_safe=False,
)
