from django.test import TestCase, Client
from django.urls import reverse
from tests.test_conf import populate_test_db

# import pytest
client = Client()


class TestsProfiles(TestCase):

    def test_index(self):
        print("TestsProfiles.test_index")
        response = client.get(reverse('profiles_index'))
        html = response.content
        assert '<title>Profiles</title>' in str(html)

    def test_profile(self):
        print("TestsProfiles.test_profile")
        populate_test_db()
        response = client.get(reverse('profile', args=['test']))
        html = response.content
        assert '<title>test</title>' in str(html)
