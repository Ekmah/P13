from django.test import TestCase, Client
from django.urls import reverse

# import pytest
client = Client()


class TestsProfiles(TestCase):

    def test_index(self):
        response = client.get(reverse('index'))
        html = response.content
        assert '<title>Holiday Homes</title>' in str(html)
