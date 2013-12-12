from farmers.models import Farmer, Receipt, Farm, Crop
from farmers.serializers import FarmerSerializer, ReceiptSerializer, FarmSerializer, CropSerializer
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
    filter_fields = ('farm_id', 'parish')

class CropViewSet(viewsets.ModelViewSet):
    """
    This view shows Crops on a Farm
    """

    queryset = Crop.objects.all()
    serializer_class = CropSerializer
    filter_fields = ('crop_name', 'common_name')
