from django.test import TestCase

from django.test import Client


class RenovationCostSiteTest(TestCase):
    def setUp(self):
        self.client = Client()

    def test_main_view(self):
        response = self.client.get('/renovation_cost')
        self.assertEqual(response.status_code, 200)



