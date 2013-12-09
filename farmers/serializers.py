from django.forms import widgets
from rest_framework import serializers
from farmers.models import Farmer, Receipt
from django.contrib.auth.models import User

class FarmerSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.Field(source='owner.username')
#    highlight = serializers.HyperlinkedIdentityField(view_name='farmer-highlight', format='html')

    class Meta:
        model = Farmer
        fields = ('url','farmer_idx','farmer_id','first_name','last_name','alias','res_address', 'res_parish','tel_number','cell_number','verified_status','dob','agri_activity','owner')


class UserSerializer(serializers.HyperlinkedModelSerializer):
    farmers = serializers.HyperlinkedRelatedField(many=True, view_name='farmer-detail')

    class Meta:
        model = User
        fields = ('url', 'username', 'farmers')


class ReceiptSerializer(serializers.HyperlinkedModelSerializer):
	receipts = serializers.HyperlinkedRelatedField(many=True, view_name='receipt-detail')

	class Meta:
		model = Receipt
		fields = ('farmer_idx', 'receipt_no', 'rec_range1', 'rec_range2', 'investigation_status', 'remarks')
