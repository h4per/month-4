from django.test import TestCase, Client
from django.urls import reverse


class PostsTestCase(TestCase):
    def setUp(self):
        self.client = Client()


    def test_index_bek(self):
        response = self.client.get(reverse("index-bek"))

        self.assertTemplateUsed(response, 'posts/index.html')
        self.assertEqual(response.status_code, 200)


    def test_get_contacts(self):
        response = self.client.get(reverse('contacts'))

        self.assertTemplateUsed(response, 'posts/contacts.html')
        self.assertEqual(response.status_code, 200)


    def test_get_about(self):
        response = self.client.get(reverse('about'))

        self.assertTemplateUsed(response, 'posts/abourt.html')
        self.assertEqual(response.status_code, 200)

    