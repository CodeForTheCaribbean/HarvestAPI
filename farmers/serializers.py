from django.forms import widgets
from rest_framework import serializers
from farmers.models import Farmer, Receipt, Farm, Crop, Livestock, Price
from django.contrib.auth.models import User

class FarmerSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.Field(source='owner.username')
    receipts = serializers.HyperlinkedRelatedField(many=True, read_only=True,
                                                 view_name='receipt-detail')
    class Meta:
        model = Farmer
        fields = ('url','farmer_id','farmer_idx','first_name','last_name','alias','res_address', 'res_parish','tel_number','cell_number','verified_status','dob','agri_activity','owner', 'receipts')

class UserSerializer(serializers.HyperlinkedModelSerializer):
    farmers = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='farmer-detail')

    class Meta:
        model = User
#        model = get_user_model()
        fields = ('url', 'username', 'farmers')


class ReceiptSerializer(serializers.HyperlinkedModelSerializer):
    farmer = FarmerSerializer()
#    farmer = serializers.HyperlinkedRelatedField(view_name='farmer-detail') 

    class Meta:
        model = Receipt
        fields = ('url','farmer', 'receipt_no', 'rec_range1', 'rec_range2', 'investigation_status', 'remarks')

class FarmSerializer(serializers.HyperlinkedModelSerializer):
    farmer = serializers.RelatedField(read_only=True)
    #farmer = serializers.HyperlinkedRelatedField(view_name='farmer-detail') 

    class Meta:
        model = Farm
        fields = ('farm_address', 'farm_id', 'parish', 'district', 'extension', 'farm_size', 'lat', 'long','farmer')

class CropSerializer(serializers.HyperlinkedModelSerializer):
    farms = serializers.RelatedField(many=True, read_only=True)

    class Meta:
        model = Crop
        fields = ('crop_name','common_name','estimated_vol','variety','plant_date','count','area','status','exp_date', 'farms')

class LivestockSerializer(serializers.HyperlinkedModelSerializer):
    farms = serializers.RelatedField(many=True, read_only=True)

    class Meta:
        model = Livestock
        fields = ('livestock_name','count','capacity','stage', 'farms')

class PriceSerializer(serializers.HyperlinkedModelSerializer):
    #crop_code = serializers.RelatedField(many=True)

    class Meta:
        model = Price
        fields = ('price','public','price_point','parish','commodity','crop_code','units','variety','batch_date','published_on','extension')

