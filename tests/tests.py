from django.test import TestCase, Client
from django.urls import reverse

# import pytest
client = Client()


class Tests(TestCase):

    def test_index(self):
        print("Tests.test_index")
        response = client.get(reverse('index'))
        html = response.content
        assert '<title>Holiday Homes</title>' in str(html)
