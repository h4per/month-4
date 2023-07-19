from django.test import TestCase, Client
from django.urls import reverse


class PostsTestCase(TestCase):
    def setUp(self):
        self.client = Client()

    def test_get_contacts(self):
        response = self.client.get(reverse('contacts'))
        exp_data = "good"

        self.assertEqual(response.content.decode(), exp_data)

    def test_get_about(self):
        response = self.client.get(reverse('about'))
        exp_data = "good 2.0"

        self.assertEqual(response.content.decode(), exp_data)

    