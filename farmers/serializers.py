from django.forms import widgets
from rest_framework import serializers
from farmers.models import Farmer, LANGUAGE_CHOICES, STYLE_CHOICES
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
