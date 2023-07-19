from django.test import TestCase, Client
from django.urls import reverse


class ExampleTestCase(TestCase):
    def setUp(self):
        self.client = Client()

    def test_test_view(self):
        response = self.client.get(reverse('test-view'))
        exp_data = 'Test'

        self.assertEqual(response.content.decode(), exp_data)
    
    def test_test_view_hello(self):
        response = self.client.get(reverse('test-hello'))
        exp_data = 'hello'

        self.assertEqual(response.content.decode(), exp_data)
        self.assertEqual(response.status_code, 500)
    
    def test_test_view_goodbye(self):
        response = self.client.get(reverse('test-bye'))
        exp_data = 'goodbye'

        self.assertEqual(response.content.decode(), exp_data)