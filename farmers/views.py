import django_filters
from farmers.models import Farmer, Receipt, Farm, Crop, Livestock, Price
from farmers.serializers import FarmerSerializer, ReceiptSerializer, FarmSerializer, CropSerializer, LivestockSerializer, PriceSerializer
 
from rest_framework import generics
from rest_framework import permissions
from django.contrib.auth.models import User
from farmers.serializers import UserSerializer
from farmers.permissions import IsOwnerOrReadOnly
from rest_framework import renderers
from rest_framework.decorators import api_view
from rest_framework.reverse import reverse
from rest_framework import renderers
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.decorators import link
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import SessionAuthentication


class FarmerViewSet(viewsets.ModelViewSet):
    """
    This view set automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` Farmers.

    """
    queryset = Farmer.objects.all()
    serializer_class = FarmerSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly,)
    filter_fields = ('farmer_idx','farmer_id','first_name','last_name','alias','res_address', 'res_parish','tel_number','cell_number','verified_status','dob','agri_activity')


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This view set automatically provides `list` and `detail`  on Users .
    """
    queryset = User.objects.all()
    authentication_classes = (SessionAuthentication,)
    permission_classes = (IsAuthenticated,)
    serializer_class = UserSerializer

class ReceiptViewSet(viewsets.ModelViewSet):
    """
    This view set automatically provides `list` and `detail` on Receipts.
    """
    queryset = Receipt.objects.all()
    serializer_class = ReceiptSerializer
    filter_fields = ('farmer','receipt_no', 'rec_range1', 'rec_range2', 'investigation_status', 'remarks')

class FarmViewSet(viewsets.ModelViewSet):
    """
    This view show Farmer's Farm
    """
    queryset = Farm.objects.all()
    serializer_class = FarmSerializer
    filter_fields = ('farm_id', 'parish', 'farmer')

class CropFilter(django_filters.FilterSet):

    class Meta:
        model = Crop
        fields = ['crop_name', 'common_name', 'farm','farm__farm_id']

class CropViewSet(viewsets.ModelViewSet):
    """
    This view shows Crops on a Farm
    """

    queryset = Crop.objects.all()
    serializer_class = CropSerializer
    filter_class = CropFilter

class LivestockFilter(django_filters.FilterSet):

    class Meta:
        model = Livestock
        fields = ['livestock_name', 'farm','farm__farm_id']

class LivestockViewSet(viewsets.ModelViewSet):
    """
    This view shows Livestock on a Farm
    """

    queryset = Livestock.objects.all()
    serializer_class = LivestockSerializer
    filter_class = LivestockFilter

class PriceFilter(django_filters.FilterSet):

    class Meta:
        model = Price
        fields = ['crop_name','crop_code','location','low','high','most_freq','week_ending']

class PriceViewSet(viewsets.ModelViewSet):
    """
    This view shows Crop Prices
    """

    queryset = Price.objects.all()
    serializer_class = PriceSerializer
    filter_class = PriceFilter

