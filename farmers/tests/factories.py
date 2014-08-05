import factory
from .. import models
from django.contrib.auth.models import User
from datetime import datetime
import pytz

class UserFactory(factory.django.DjangoModelFactory):
  class Meta:
      model = User

  first_name = factory.Sequence(lambda n: "First%s" % n)
  last_name = factory.Sequence(lambda n: "Last%s" % n)
  email = factory.Sequence(lambda n: "email%s@example.com" % n)
  username = factory.Sequence(lambda n: "email%s@example.com" % n)
  password = "password"

class FarmerFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Farmer

    farmer_idx = '123455'
    farmer_id = factory.Sequence(lambda n: '%d' % n)
    first_name = 'Erica'
    last_name = 'Kwan'
    dob = datetime.now(pytz.utc)
    owner = factory.SubFactory(UserFactory)

class ReceiptFactory(factory.django.DjangoModelFactory):
  class Meta:
      model = models.Receipt

  receipt_no = factory.Sequence(lambda n: '%d' % n)
  farmer = factory.SubFactory(FarmerFactory)


class FarmFactory(factory.django.DjangoModelFactory):
  class Meta:
      model = models.Farm

  farmer = factory.SubFactory(FarmerFactory)
  farm_address = '155 9th st.'
  farm_id = factory.Sequence(lambda n: '%d' % n)
  parish = 'Manchester'
  farm_status = 'YES'
