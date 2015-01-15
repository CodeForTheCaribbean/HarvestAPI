import django_filters
from farmers.models import Farmer, Receipt, Farm, Crop, Livestock, Price, RegistrationManager, RegistrationProfile
from farmers.serializers import FarmerSerializer, ReceiptSerializer, FarmSerializer, CropSerializer, LivestockSerializer, PriceSerializer
 
from rest_framework import generics
from rest_framework import permissions
from django.contrib.auth.models import *
from farmers.serializers import UserSerializer
from farmers.permissions import IsOwnerOrReadOnly
from rest_framework.decorators import api_view
from rest_framework.reverse import reverse
from rest_framework import renderers
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework import filters
from rest_framework.decorators import link

from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.authentication import SessionAuthentication, TokenAuthentication, BasicAuthentication
from django.contrib.auth import get_user_model
from rest_framework import status, serializers
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.authtoken.models import Token

from django.contrib import messages
from django.conf import settings

from django.views.decorators.csrf import csrf_protect
from django.core.context_processors import csrf
from django.shortcuts import render_to_response, get_object_or_404, render, RequestContext, redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.template import *
import hashlib, datetime, random
from django.utils import timezone

from django.views.generic.base import TemplateView
from django.views.generic.edit import FormView

from farmers.signals import *
from farmers.forms import RegistrationForm, PasswordChangeForm, PasswordResetForm, SetPasswordForm

from django.contrib.sites.models import RequestSite
from django.contrib.sites.models import Site
from django.contrib.auth.views import password_reset, password_reset_confirm
from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives
from django.core import signing
from django.utils.http import base36_to_int
from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache

from password_policies.views import *
from password_policies.forms import *
from password_policies.conf import settings
from password_policies.models import *

User = get_user_model()

USER_MODEL_FIELD_NAMES = [field.name for field in User._meta.fields]
USER_REQUIRED_FIELDS = set([User.USERNAME_FIELD] + list(User.REQUIRED_FIELDS))
USER_FORM_FIELDS = getattr(settings, 'USER_FORM_FIELDS', USER_REQUIRED_FIELDS)


class FarmerViewSet(viewsets.ModelViewSet):
    """
    This view set automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` Farmers.

    """
    authentication_classes = (BasicAuthentication, SessionAuthentication, TokenAuthentication)
    queryset = Farmer.objects.all()
    serializer_class = FarmerSerializer
    permission_classes = (IsAuthenticated,)#(permissions.IsAuthenticatedOrReadOnly,
                         # IsOwnerOrReadOnly,)
    filter_fields = ('farmer_idx','farmer_id','first_name','last_name','alias','res_address', 'res_parish','tel_number','cell_number','verified_status','dob','agri_activity')
    filter_backends = (filters.SearchFilter,filters.OrderingFilter,filters.DjangoFilterBackend,)
    search_fields = ('first_name', 'last_name', 'alias', 'res_parish', 'agri_activity')
    ordering_fields = ('first_name', 'last_name', 'alias', 'res_parish', 'agri_activity', 'verified_status', 'dob')

class UserViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This view set automatically provides `list` and `detail`  on Users .
    """
    queryset = User.objects.all()
    authentication_classes = (SessionAuthentication,TokenAuthentication)
    permission_classes = (IsAdminUser,)
    serializer_class = UserSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('username', 'email')

class ReceiptFilter(django_filters.FilterSet):

    parish = django_filters.CharFilter(name="farmer__res_parish")
    farmer_id = django_filters.CharFilter(name="farmer__farmer_id")

    class Meta:
        model = Receipt
        fields = ['farmer','receipt_no', 'rec_range1', 'rec_range2', 'investigation_status', 'remarks','farmer_id','parish']


class ReceiptViewSet(viewsets.ModelViewSet):
    """
    This view set automatically provides `list` and `detail` on Receipts.
    """
    queryset = Receipt.objects.all()
    permission_classes = (IsAdminUser,)
    serializer_class = ReceiptSerializer
    filter_class = ReceiptFilter
    filter_backends = (filters.SearchFilter,filters.OrderingFilter,filters.DjangoFilterBackend,)
    search_fields = ('remarks')
    ordering_fields = ('farmer', 'investigation_status')

class FarmFilter(django_filters.FilterSet):

    farmer_id = django_filters.CharFilter(name="farmer__farmer_id")
    min_size = django_filters.NumberFilter(name="farm_size", lookup_type='gte')
    max_size = django_filters.NumberFilter(name="farm_size", lookup_type='lte')
    class Meta:
        model = Farm
        fields = ['farmer_idx','farmer_id','farm_address','farm_id','parish','district','extension','farm_size','lat','long','farm_status','farmer','min_size','max_size']



class FarmViewSet(viewsets.ModelViewSet):
    """
    This view show Farmer's Farm
    """
    queryset = Farm.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = FarmSerializer
    filter_class = FarmFilter
    filter_backends = (filters.SearchFilter,filters.OrderingFilter,filters.DjangoFilterBackend,)
    search_fields = ('parish','farm_address','farm_id','farmer_idx', 'extension', 'farm_status', 'farm_size')
    ordering_fields = ('parish','district')


class CropFilter(django_filters.FilterSet):

    parish = django_filters.CharFilter(name="farm__parish")
    farm_id = django_filters.CharFilter(name="farm__farm_id")
    min_vol = django_filters.NumberFilter(name="estimated_vol", lookup_type='gte')
    max_vol = django_filters.NumberFilter(name="estimated_vol", lookup_type='lte')

    class Meta:
        model = Crop
        fields = ['crop_name', 'common_name', 'farm','farm__farm_id', 'parish', 'min_vol', 'max_vol']

class CropViewSet(viewsets.ModelViewSet):
    """
    This view shows Crops on a Farm
    """

    queryset = Crop.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = CropSerializer
    filter_class = CropFilter
    filter_backends = (filters.SearchFilter,filters.OrderingFilter,filters.DjangoFilterBackend,)
    search_fields = ('crop_name',)
    ordering_fields = ('crop_name', 'farm', 'farm_id')


class LivestockFilter(django_filters.FilterSet):

    parish = django_filters.CharFilter(name="farm__parish")
    farm_id = django_filters.CharFilter(name="farm__farm_id")

    class Meta:
        model = Livestock
        fields = ['livestock_name', 'farm','farm_id', 'parish']

class LivestockViewSet(viewsets.ModelViewSet):
    """
    This view shows Livestock on a Farm
    """

    queryset = Livestock.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = LivestockSerializer
    filter_class = LivestockFilter
    filter_backends = (filters.SearchFilter,filters.OrderingFilter,filters.DjangoFilterBackend,)
    search_fields = ('livestock_name',)
    ordering_fields = ('livestock_name', 'farm', 'farm_id')


class PriceFilter(django_filters.FilterSet):

    min_price = django_filters.NumberFilter(name="price", lookup_type='gte')
    max_price = django_filters.NumberFilter(name="price", lookup_type='lte')

    class Meta:
        model = Price
        fields = ['price_id','price','public','price_point','parish','commodity','crop_code','units','variety','batch_date','published_on','extension','min_price','max_price',]

class PriceViewSet(viewsets.ModelViewSet):
    """
    This view shows Crop Prices
    """

    queryset = Price.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = PriceSerializer
    filter_class = PriceFilter
    filter_backends = (filters.SearchFilter,filters.OrderingFilter,filters.DjangoFilterBackend,)
    search_fields = ('commodity', 'crop_code', 'price_point', 'extension', 'parish')
    ordering_fields = ('commodity', 'crop_code', 'price_point', 'extension', 'parish')


#@api_view(['POST'])
#def register(request):
#    DEFAULTS = {
        # you can define any defaults that you would like for the user, here
#    }
#    serialized = UserSerializer(data=request.DATA)
#    if serialized.is_valid():
#        user_data = {field: data for (field, data) in request.DATA.items() if field in VALID_USER_FIELDS}
#        user_data.update(DEFAULTS)
#        user = get_user_model().objects.create_user(
#            **user_data
#        )
#        return Response(UserSerializer(instance=user).data, status=status.HTTP_201_CREATED)
#    else:
#        return Response(serialized._errors, status=status.HTTP_400_BAD_REQUEST)

#@csrf_protect
#def register_here(request):
#    """ User sign up form """
#    if request.method == 'POST':
#        form = RegistrationForm(request.POST)
#        if form.is_valid():
#            form.save()
#            return HttpResponseRedirect('/user/register/complete')
        
#    args={}
            
    # builds the form securely
#    args.update(csrf(request))
        
#    args['form'] = RegistrationForm()
#    return render_to_response('registration/registration_form.html', args) 


#def register_success(request):
#    return render_to_response('registration/registration_complete.html')

"""
    Views which allows users to create and activate accounts.
"""

class _RequestPassingFormView(FormView):
    """
    A version of FormView which passes extra arguments to certain methods,
    notably passing the HTTP request nearly everywhere, to enable
    finer-grained processing.
    """
    def get(self, request, *args, **kwargs):
        # Pass request to get_form_class and get_form for per-request
        # form control
        form_class = self.get_form_class(request)
        form = self.get_form(form_class)
        return self.render_to_response(self.get_context_data(form=form))
    
    def post(self, request, *args, **kwargs):
        # Pass request to get_form_class and get_form for per-request
        # form control.
        form_class = self.get_form_class(request)
        form = self.get_form(form_class)
        
        if form.is_valid():
            # Pass request to form_valid.
            return self.form_valid(request, form)
        else:
            return self.form_invalid(form)
        
    def get_form_class(self, request=None):
        return super(_RequestPassingFormView, self).get_form_class()
    
    def get_form_kwargs(self, request=None, form_class=None):
        return super(_RequestPassingFormView, self).get_form_kwargs()
    
    def get_initial(self, request=None):
        return super(_RequestPassingFormView, self).get_initial()
    
    def get_success_url(self, request=None, user=None):
        # We need to be able to use the request and the new user when
        # constructing success_url.
        return super(_RequestPassingFormView, self).get_success_url()
    
    def form_valid(self, form, request=None):
        return super(_RequestPassingFormView, self).form_valid(form)
    
    def form_invalid(self, form, request=None):
        return super(_RequestPassingFormView, self).form_invalid(form)    


class RegistrationView(_RequestPassingFormView):
    """
        Base class for user registration views.
    """
    disallowed_url = 'registration_disallowed'
    form_class = RegistrationForm
    http_method_names = ['get', 'post', 'head', 'options', 'trace']
    success_url = None
    template_name = 'registration/registration_form.html'
    
    def dispatch(self, request, *args, **kwargs):
        """
        Check that user signup is allowed before even bothering to
        dispatch or do other processing.
                
        """        
        if not self.registration_allowed(request):
            return redirect(self.disallowed_url)
        return super(RegistrationView, self).dispatch(request, *args, **kwargs)
    
    def form_valid(self, request, form):
        new_user = self.register(request, **form.cleaned_data)
        success_url = self.get_success_url(request, new_user)
        
        # success_url may be a simple string, or a tuple providing the
        # full argument set for redirect(). Attempting to unpack it
        # tells us which one it is.        
        try:
            to, args, kwargs = success_url
            return redirect(to, *args, **kwargs)
        except ValueError:
            return redirect(success_url)
        
    def registration_allowed(self, request):
        """
        Override this to enable/disable user registration, either
        globally or on a per-request basis.
        """   
        return getattr(settings, 'REGISTRATION_OPEN', True)
        
    def register(self, request, **cleaned_data):
        """
        Implement user-registration logic here. Access to both the
        request and the full cleaned_data of the registration form is
        available here.        
        """
        user_args = {'password': cleaned_data['password1']}
        
        for field in USER_FORM_FIELDS:
            if field in cleaned_data:
                user_args[field] = cleaned_data[field]
        
        if Site._meta.installed:
            site = Site.objects.get_current()
        else:
            site = RequestSite(request)
        
        new_user = RegistrationProfile.objects.create_inactive_user(user_args, 
                                                                    site)
        
        user_registered.send(sender=self.__class__,
                             user = new_user,
                             request = request)
        return new_user     
    
    def get_success_url(self, request, user):
            return ('registration_complete', (), {})    


class ActivationView(TemplateView):
    """
    Base class for user activation views.
    """    
    http_method_names = ['get']
    template_name1 = 'registration/activate.html'
    
    def get(self, request, *args, **kwargs):
        activated_user = self.activate(request, *args, **kwargs)
        if activated_user:
            user_activated.send(sender=self.__class__,
                                user=activated_user,
                                request=request)
            success_url = self.get_success_url(request, activated_user)
            
            try:
                to, args, kwargs = success_url
                return redirect(to, *args, **kwargs)
            except ValueError:
                return redirect(success_url)
        return super(ActivationView, self).get(request, *args, **kwargs)
    
    def activate(self, request, activation_key):
        activated_user = RegistrationProfile.objects.activate_user(activation_key)
        if activated_user:
            user_activated.send(sender=self.__class__,
                                user=activated_user,
                                request=request)
        return activated_user
    
    
    def get_success_url(self, request, user):
        return ('registration_activation_complete', (), {})