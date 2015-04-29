from django.forms import widgets
from rest_framework import serializers
from farmers.models import Farmer, Receipt, Farm, Crop, Livestock, Price
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


class FarmerPrivateSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.Field(source='owner.username')
    receipts = serializers.HyperlinkedRelatedField(many=True, read_only=True,
                                                 view_name='receipt-detail')
    class Meta:
        model = Farmer
        fields = ('url','farmer_id','farmer_idx', 'res_parish','verified_status','agri_activity','owner')

    def to_internal_value(self, data):
        farmer_id = data.get('farmer_id')
        farmer_idx = data.get('farmer_idx')
	res_parish = data.get('res_parish')
	verified_status = data.get('verified_status')
	agri_activity = data.get('agri_activity')
	owner = data.get('owner')

        if not farmer_id:
            raise ValidationError({
                'farmer_id': 'This field is required.'
            })
        if not res_parish:
            raise ValidationError({
                'res_parish': 'This field is required.'
            })
        if not agri_activity:
            raise ValidationError({
                'agri_activity': 'This field is required.'
            })
        if len(farmer_id) > 10:
            raise ValidationError({
                'farmer_id': 'May not be more than 10 characters.'
            })

        # Return the validated values. This will be available as
        # the `.validated_data` property.
        return {
            'farmer_id': farmer_id,
	    'farmer_idx':farmer_idx,
	    'res_parish':res_parish,
	    'verified_status':verified_status,
	    'agri_activity':agri_activity,
	    #'owner':owner
        }

    def to_representation(self, obj):
        return {
            'farmer_id': obj.farmer_id,
            'farmer_idx': obj.farmer_idx,
            'res_parish': obj.res_parish,
            'verified_status': obj.verified_status,
            'agri_activity': obj.agri_activity,
     # this field is not serializable      #'owner': obj.owneddr,
        }

    def create(self, validated_data):
        return Farmer.objects.create(**validated_data)


class FarmerSerializer(serializers.HyperlinkedModelSerializer):


    owner = serializers.Field(source='owner.username')
#    receipts = serializers.HyperlinkedRelatedField(many=True, read_only=True,
#                                                 view_name='receipt-detail')
    class Meta:
        model = Farmer
        fields = ('url','farmer_id','farmer_idx','first_name','last_name','alias','res_address', 'res_parish','tel_number','cell_number','verified_status','dob','agri_activity','owner')

    def to_internal_value(self, data):
        farmer_id = data.get('farmer_id')
        first_name = data.get('first_name')
        last_name = data.get('last_name')
        dob = data.get('dob')
        farmer_idx = data.get('farmer_idx')
	alias = data.get('alias')
	res_address = data.get('res_address')
	res_parish = data.get('res_parish')
	tel_number = data.get('tel_number')
	cell_number = data.get('cell_number')
	verified_status = data.get('verified_status')
	agri_activity = data.get('agri_activity')
	owner = data.get('owner')

        if not farmer_id:
            raise ValidationError({
                'farmer_id': 'This field is required.'
            })
        if not first_name:
            raise ValidationError({
                'first_name': 'This field is required.'
            })
        if not last_name:
            raise ValidationError({
                'last_name': 'This field is required.'
            })
        if len(farmer_id) > 10:
            raise ValidationError({
                'farmer_id': 'May not be more than 10 characters.'
            })

        # Return the validated values. This will be available as
        # the `.validated_data` property.
        return {
            'farmer_id': farmer_id,
            'first_name': first_name,
            'last_name': last_name,
            'dob':dob,
	    'farmer_idx':farmer_idx,
	    'alias':alias,
	    'res_address':res_address,
	    'res_parish':res_parish,
	    'tel_number':tel_number,
	    'cell_number':cell_number,
	    'verified_status':verified_status,
	    'agri_activity':agri_activity,
	    #'owner':owner
        }

    def to_representation(self, obj):
        return {
            'farmer_id': obj.farmer_id,
            'farmer_idx': obj.farmer_idx,
            'first_name': obj.first_name,
            'last_name': obj.last_name,
            'alias': obj.alias,
            'dob':obj.dob,
            'res_address': obj.res_address,
            'res_parish': obj.res_parish,
            'tel_number': obj.tel_number,
            'cell_number': obj.cell_number,
            'verified_status': obj.verified_status,
            'agri_activity': obj.agri_activity,
     # this field is not serializable      #'owner': obj.owneddr,
        }

    def create(self, validated_data):
        return Farmer.objects.create(**validated_data)


class UserSerializer(serializers.HyperlinkedModelSerializer):
    farmers = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='farmer-detail')

    class Meta:
        model = User
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

    def to_internal_value(self, data):
        farm_id = data.get('farm_id')
        farm_address = data.get('farm_address')
	parish = data.get('parish')
	district = data.get('district')
	extension = data.get('extension')
	farm_size = data.get('farm_size')
	lat = data.get('lat')
	long = data.get('long')
	farmer = data.get('farmer')

        if not parish:
            raise ValidationError({
                'parish': 'This field is required.'
            })
        if not district:
            raise ValidationError({
                'district': 'This field is required.'
            })
        if not extension:
            raise ValidationError({
                'extension': 'This field is required.'
            })
        if len(farm_id) > 10:
            raise ValidationError({
                'farm_id': 'May not be more than 10 characters.'
            })

        # Return the validated values. This will be available as
        # the `.validated_data` property.
        return {
            'farm_id': farm_id,
	    'farm_address':farm_address,
	    'parish':parish,
	    'district':district,
	    'extension':extension,
	    'farm_size':farm_size,
	    'lat':lat,
	    'long':long
	    #'owner':owner
        }

    def to_representation(self, obj):
        return {
            'farm_id': obj.farm_id,
            'farm_address': obj.farm_address,
            'parish': obj.parish,
            'district': obj.district,
            'extension': obj.extension,
            'farm_size': obj.farm_size,
            'lat': obj.lat,
            'long': obj.long
        }

    def create(self, validated_data):
        return Farmer.objects.create(**validated_data)


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

