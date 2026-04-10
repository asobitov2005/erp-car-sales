from rest_framework import status
from rest_framework.test import APITestCase

from api.models.Country import Country


class ApiSmokeTests(APITestCase):
    def test_country_list_endpoint_returns_created_country(self):
        Country.objects.create(name='Uzbekistan')

        response = self.client.get('/api/v1/countries/')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]['name'], 'Uzbekistan')
