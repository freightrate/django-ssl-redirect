from django.conf import settings
from django.core.urlresolvers import reverse
from django.test import Client, TestCase


class SecureDefaultTestCase(TestCase):
    def setUp(self):
        self.client = Client()

    def test_secure_url(self):
        url = reverse('secure_page')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 301)

    def test_unsecure_url(self):
        url = reverse('unsecure_page')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_default_url(self):
        url = reverse('default_page')
        response = self.client.get(url)
