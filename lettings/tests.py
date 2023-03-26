from django.test import TestCase, Client
from django.urls import reverse
from tests.test_conf import *

# import pytest
client = Client()


class TestsLettings(TestCase):

    def test_index(self):
        response = client.get(reverse('lettings_index'))
        html = response.content
        assert '<title>Lettings</title>' in str(html)

    def test_profile(self):
        populate_test_db()
        response = client.get(reverse('letting', args=[1]))
        html = response.content
        assert '<title>title</title>' in str(html)
