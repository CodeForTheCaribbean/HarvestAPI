"""
API tests
"""

from django.test import TestCase
from factories import FarmerFactory, FarmFactory, ReceiptFactory
from django.core.urlresolvers import reverse
from rest_framework import status
from .. import models

class ApiTest(TestCase):
  """
  test /farmers
  """
  def test_farmers_list(self):
    FarmerFactory(first_name='Grace', last_name='Hopper')
    FarmerFactory(res_address='13 main st', res_parish='Saint Mary')
    url = reverse('farmer-list')
    response = self.client.get(url)
    self.assertEqual(response.status_code, status.HTTP_200_OK)
    self.assertEqual(response.data['count'], 2)
    self.assertEqual(response.data['results'][0]['first_name'], 'Grace')
    self.assertEqual(response.data['results'][1]['res_parish'], 'Saint Mary')

  """
  test /farmers/id
  """
  def test_farmer_details(self):
    farmer = FarmerFactory(first_name='Maria', last_name='Telkes')
    url = reverse('farmer-detail', args=farmer.farmer_id)
    response = self.client.get(url)
    self.assertEqual(response.status_code, status.HTTP_200_OK)
    self.assertEqual(response.data['last_name'], 'Telkes')
