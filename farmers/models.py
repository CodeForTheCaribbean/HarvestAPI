import datetime
import hashlib
import random
import re

from django.db import models
from rest_framework.authtoken.models import Token

from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from django.utils import timezone

from django.conf import settings
from django.db import transaction
from django.template.loader import render_to_string
from django.utils.translation import ugettext_lazy as _
from django.core.mail import EmailMultiAlternatives

from django.utils import *

User = get_user_model()

try:
    from django.utils.timezone import now as datetime_now
except ImportError:
    datetime_now = datetime.datetime.now


SHA1_RE = re.compile('^[a-f0-9]{40}$')


@receiver(post_save, sender=get_user_model())
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)


class Farmer(models.Model):

    farmer_idx =  models.CharField(max_length=100, blank=False, default='')
    farmer_id =  models.CharField(max_length=100, blank=False, default='', primary_key=True)
    first_name = models.CharField(max_length=100, null=True, default='')
    last_name = models.CharField(max_length=100, null=True, default='')
    alias = models.CharField(max_length=100, null=True, default='')
    res_address = models.CharField(max_length=200, null=True, default='')
    res_parish = models.CharField(max_length=20, null=True, default='')
    tel_number = models.CharField(max_length=20, null=True, default='')
    cell_number = models.CharField(max_length=20, null=True, default='')
    verified_status = models.CharField(max_length=3, null=True, default='')
    dob = models.DateTimeField()
    agri_activity = models.CharField(max_length=150, null=True, default='')
    owner = models.ForeignKey('auth.User', related_name='farmers', default='1', null=True)
    last_updated = models.DateTimeField(auto_now_add=True, null=True)
#    receipts = models.ForeignKey('Receipt', related_name='receipts', null=True)

    class Meta:
        ordering = ('last_updated',)

    def __unicode__(self):
            return 'Farm Activity: %s' % (self.agri_activity)

class Receipt(models.Model):

    receipt_no =  models.CharField(max_length=100, null=False, default='', primary_key=True)
    rec_range1 = models.CharField(max_length=100, null=True, default='')
    rec_range2 = models.CharField(max_length=100, null=True, default='')
    investigation_status = models.CharField(max_length=100, null=True, default='')
    last_updated = models.DateTimeField(auto_now_add=True, null=True)
    remarks = models.CharField(max_length=200, null=True, default='')
    farmer = models.ForeignKey(Farmer)

    class Meta:
        ordering = ('last_updated',)

    def __unicode__(self):
        return 'Receipt no: %s' % (self.receipt_no)

class Farm(models.Model):

#    farmer_id = models.CharField(max_length=100, null=False, default='')
    farmer_idx = models.CharField(max_length=100, null=False, default='')
    farm_address = models.CharField(max_length=255, default='')
    farm_id = models.CharField(max_length=100, default='', primary_key=True)
    parish = models.CharField(max_length=30, default='')
    district = models.CharField(max_length=50, default='')
    extension = models.CharField(max_length=50, default='')
    farm_size = models.CharField(max_length=50, default='', null=True)
    lat = models.CharField(max_length=50, default='', null=True)
    long = models.CharField(max_length=50, default='', null=True)
    farm_status = models.CharField(max_length=50, default='')
    farmer = models.ForeignKey(Farmer)

    class Meta:
        ordering = ('district',)

    def __unicode__(self):
        return 'Farm Info - Parish %s Address %s Farm Status %s' % (self.parish, self.farm_address, self.farm_status)

class Crop(models.Model):

    crop_name = models.CharField(max_length=100, default='')
    common_name = models.CharField(max_length=30, default='', null=True)
    estimated_vol = models.DecimalField(max_digits=10, default='', null=True, decimal_places=2)
    variety = models.CharField(max_length=50, default='', null=True)
    plant_date = models.CharField(max_length=50, default='', null=True)
    count = models.CharField(max_length=50, default='', null=True)
    area = models.CharField(max_length=50, default='', null=True)
    status = models.CharField(max_length=50, default='', null=True)
    exp_date = models.CharField(max_length=50, default='', null=True)
    farm = models.ForeignKey(Farm)

    class Meta:
        ordering = ('crop_name',)


class Livestock(models.Model):

    livestock_name = models.CharField(max_length=100, default='')
    count = models.CharField(max_length=50, default='', null=True)
    capacity = models.CharField(max_length=50, default='', null=True)
    stage = models.CharField(max_length=50, default='', null=True)
    farm = models.ForeignKey(Farm)

    class Meta:
        ordering = ('livestock_name',)

class Price(models.Model):

    price_id =  models.CharField(max_length=100, null=False, default='', primary_key=True)
    price  = models.DecimalField(max_digits=10, default='', null=True, decimal_places=2)
    public = models.CharField(max_length=10, default='', null=True)
    price_point = models.CharField(max_length=50, default='', null=True)
    parish = models.CharField(max_length=50, default='', null=True)
    commodity = models.CharField(max_length=50, default='', null=True)
    crop_code = models.CharField(max_length=50, default='', null=True)
    units = models.CharField(max_length=50, default='', null=True)
    variety = models.CharField(max_length=50, default='', null=True)
    batch_date = models.DateField(max_length=50, default='', null=True)
    published_on = models.DateField(max_length=50, default='', null=True)
    extension = models.CharField(max_length=50, default='', null=True)

    class Meta:
        ordering = ('published_on',)

class RegistrationManager(models.Manager):
    
    def activate_user(self, activation_key):
        """
        Validate an activation key and activate the corresponding
        ``User`` if valid.
                
        If the key is valid and has not expired, return the ``User``
        after activating.
                
        If the key is not valid or has expired, return ``False``.
        
        If the key is valid but the ``User`` is already active,
        return ``False``.
                
        To prevent reactivation of an account which has been
        deactivated by site administrators, the activation key is
        reset to the string constant ``RegistrationProfile.ACTIVATED``
        after successful activation.
        
        """        
        if SHA1_RE.search(activation_key):
            try:
                profile = self.get(activation_key=activation_key)
            except self.model.DoesNotExist:
                return False
            if not profile.activation_key_expired():
                user=profile.user
                user.is_active = True
                user.save()
                profile.activation_key = self.model.ACTIVATED
                profile.save()
                return user
            return False
        
    def create_inactive_user(self, user_args, site, send_email=True):
        """
        Create a new, inactive ``User``, generate a
        ``RegistrationProfile`` and email its activation key to the
        ``User``, returning the new ``User``.
            
        By default, an activation email will be sent to the new
        user. To disable this, pass ``send_email=False``.
        """            
        new_user = User.objects.create_user(**user_args)
        new_user.is_active = False
        new_user.save()
        
        # ensure username for cases where email is the USERNAME_FIELD
        if not new_user.username or new_user.username is None:
            new_user.username = get_or_generate_username(new_user)
            new_user.save()        
            
        registration_profile = self.create_profile(new_user)
            
        if send_email:
            registration_profile.send_activation_email(site)
                
        return new_user
    create_inactive_user = transaction.commit_on_success(create_inactive_user)
        
        
    def create_profile(self, user):
        """
        Create a ``RegistrationProfile`` for a given
        ``User``, and return the ``RegistrationProfile``.
        
        The activation key for the ``RegistrationProfile`` will be a
        SHA1 hash, generated from a combination of the ``User``'s
        username and a random salt.
        
        """            
        salt = hashlib.sha1(str(random.random())).hexdigest()[:5]
        username = user.username
        if isinnstance(username, unicode):
            username = username.encode('utf-8')
        activation_key = hashlib.sha1(salt+username).hexdigest()
        return self.create(user=user,
                           activation_key=activation_key)
        
        
    def delete_expired_users(self):
        for profile in self.all():
            try:
                if profile.activation_key_expired():
                    user = profile.user
                    if not user.is_active:
                        user.delete()
                        profile.delete()
            except User.DoesNotExist:
                profile.delete()
            
class RegistrationProfile(models.Model):    
    """
        A simple profile which stores an activation key for use during
        user account registration.
        
        Generally, you will not want to interact directly with instances
        of this model; the provided manager includes methods
        for creating and activating new accounts, as well as for cleaning
        out accounts which have never been activated.
        
        While it is possible to use this model as the value of the
        ``AUTH_PROFILE_MODULE`` setting, it's not recommended that you do
        so. This model's sole purpose is to store data temporarily during
        account registration and activation.
        
    """    
    ACTIVATED = u"ALREADY_ACTIVATED"
    
    user = models.ForeignKey(User, unique=True, related_name= 'user')
    activation_key = models.CharField(_('activation_key'), max_length=40)
    ###    key_expires = models.DateTimeField(default=datetime.date.today()) 
    
    objects = RegistrationManager()
    
    def __unicode__(self):
        return u"Registration information for %s" % self.user

    class Meta:
        verbose_name = _('user profile')
        verbose_name_plural = _('User profiles')
        
    def activation_key_expired(self):
        """
        Determine whether this ``RegistrationProfile``'s activation
        key has expired, returning a boolean -- ``True`` if the key
        has expired.
                
        Key expiration is determined by a two-step process:
                
        1. If the user has already activated, the key will have been
        reset to the string constant ``ACTIVATED``. Re-activating
        is not permitted, and so this method returns ``True`` in
        this case.
        
        2. Otherwise, the date the user signed up is incremented by
        the number of days specified in the setting
        ``ACCOUNT_ACTIVATION_DAYS`` (which should be the number of
        days after signup during which a user is allowed to
        activate their account); if the result is less than or
        equal to the current date, the key has expired and this
        method returns ``True``.
                
        """
        expiration_date = datetime.timedelta(days=settings.ACCOUNT_ACTIVATION_DAYS)
        return self.activation_key == self.ACTIVATED or \
               (self.user.date_joined + expiration_date <= datetime_now())
    activation_key_expired.boolean = True
        
    
    def send_activation_email(self, site):
        """
                Send an activation email to the user associated with this
                ``RegistrationProfile``.
                
                The activation email will make use of two templates:
        
                ``registration/activation_email_subject.txt``
                    This template will be used for the subject line of the
                    email. Because it is used as the subject line of an email,
                    this template's output **must** be only a single line of
                    text; output longer than one line will be forcibly joined
                    into only a single line.
        
                ``registration/activation_email.txt``
                    This template will be used for the body of the email.
        
                These templates will each receive the following context
                variables:
        
                ``activation_key``
                    The activation key for the new account.
        
                ``expiration_days``
                    The number of days remaining during which the account may
                    be activated.
        
                ``site``
                    An object representing the site on which the user
                    registered; depending on whether ``django.contrib.sites``
                    is installed, this may be an instance of either
                    ``django.contrib.sites.models.Site`` (if the sites
                    application is installed) or
                    ``django.contrib.sites.models.RequestSite`` (if
                    not). Consult the documentation for the Django sites
                    framework for details regarding these objects' interfaces.
        """ 
        ctx_dict = {'activation_key': self.activation_key,
                    'expiration_days': settings.ACCOUNT_ACTIVATION_DAYS,
                    'site': site,
                    'user': self.user}
        subject = render_to_string('registration/activation_email_subject.txt',
                                   cxt_dict)
        
        ### Email subject should not contain newlines
        subject = ''.join(subject.splitlines())
        
        message_txt = render_to_string('registration/activation_email.txt',
                                   cxt_dict)
        
        message_html = render_to_string('registration/activation_email.html',
                                                ctx_dict)        
        
        message = EmailMultiAlternatives(
            subject,
            message_txt,
            settings.DEFAULT_FROM_EMAIL,
            (self.user.email,)
        )
        
        message.attach_alternative(
            message_html,
            'text/html'
        )
        message.send()