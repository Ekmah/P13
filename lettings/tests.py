from django.test import TestCase, Client
from django.urls import reverse
from tests.test_conf import *

# import pytest
client = Client()


class TestsLettings(TestCase):

    def test_index(self):
        print("TestsLettings.test_index")
        response = client.get(reverse('lettings_index'))
        html = response.content
        assert '<title>Lettings</title>' in str(html)

    def test_letting(self):
        print("TestsLettings.test_letting")
        populate_test_db()
        response = client.get(reverse('letting', args=[1]))
        html = response.content
        assert '<title>title</title>' in str(html)
