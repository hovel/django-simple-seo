# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from random import choice
from string import ascii_letters
import xml.etree.ElementTree as ET

from django.test import TestCase
from django.utils.encoding import force_text
from simpleseo.models import SeoMetadata
from django.conf import settings

from six.moves.urllib.parse import urlparse, unquote


class TestSimpleseoMixin(object):
    location_list = []
    exclude_list = []

    def __init__(self, *args, **kwargs):
        if not isinstance(self, TestCase):
            raise Exception(
                'TestSimpleseoMixin is a mixin, not a test. Do not try to run '
                'it directly. Example: TestClass(TestSimpleseoMixin, TestCase)'
            )
        super(TestSimpleseoMixin, self).__init__(*args, **kwargs)

    def test_simpleseo(self):
        raw_sitemap = self.client.get('/sitemap.xml')
        if raw_sitemap.status_code == 200:
            sitemap = ET.fromstring(raw_sitemap.content)
            namespaces = {'sm': 'http://www.sitemaps.org/schemas/sitemap/0.9'}
            for loc in sitemap.findall('sm:url/sm:loc', namespaces=namespaces):
                path = urlparse(loc.text).path
                if any(exclude in path for exclude in self.exclude_list):
                    continue
                self.location_list.append(path)

        for path in self.location_list:
            path = force_text(unquote(path))
            seo = SeoMetadata.objects.create(
                path=path, lang_code=settings.LANGUAGE_CODE[:2],
                title=''.join(choice(ascii_letters) for _ in range(20)),
                description=''.join(choice(ascii_letters) for _ in range(120)),
            )
            print('Test path: {0}'.format(path))
            response = self.client.get(path, follow=True)
            if response.status_code == 404:
                print('Warning: page not found')
            content = force_text(response.content[:1000])
            self.assertIn(seo.title, content)
            self.assertIn(seo.description, content)
