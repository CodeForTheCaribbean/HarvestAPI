"""
Model tests
"""

from django.test import TestCase
from factories import FarmerFactory, FarmFactory, ReceiptFactory

class FarmerModelsTest(TestCase):
    def test_farmer_creation(self):
      """
      Check that unicode() returns the proper string when only first name and last
      name are set
      """
      farmer = FarmerFactory(first_name='Marie', last_name='Curie')
      self.assertEqual(farmer.__unicode__(), ' Name - Marie Curie')

      """
      Check that unicode() returns the proper string when first name, last
      name and cell number are set
      """
      farmer = FarmerFactory(first_name='Mary', last_name='Anning', cell_number='18765551234')
      self.assertEqual(farmer.__unicode__(), ' Name - Mary Anning Cell 18765551234')

      """
      Check that unicode() returns the proper string when first name, last
      name, alias and cell number are set
      """
      farmer = FarmerFactory(first_name='Shirley', last_name='Jackson',
                             alias='Shirley Ann', cell_number='18765559876')
      self.assertEqual(farmer.__unicode__(), ' Name - Shirley "Shirley Ann" Jackson Cell 18765559876')

    """
    Check that unicode() returns the proper string
    """
    def test_receipt_creation(self):
      receipt = ReceiptFactory(receipt_no='145567')
      self.assertEqual(receipt.__unicode__(), 'Receipt no: 145567')

    """
    Check that unicode() returns the proper string
    """
    def test_farm_creation(self):
      farm = FarmFactory(parish='Manchester', farm_address='12 8th Ave.',farm_status='Yes')
      self.assertEqual(farm.__unicode__(), 'Farm Info - Parish Manchester Address 12 8th Ave. Farm Status Yes')
