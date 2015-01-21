
from django import forms
from django.contrib.auth.models import User
#from django.contrib.auth.forms import UserCreationForm
from django.core import validators
from django.utils.translation import ugettext_lazy as _

class RegistrationForm(forms.Form):
    username = forms.CharField(
                widget = forms.TextInput
                        (attrs = {'class': "form-control",
                                  'placeholder': 'Username *'}))

    email= forms.EmailField(
            widget = forms.TextInput
                    (attrs = {'class': "form-control",
                              'placeholder': 'Email *'}))

    password1 = forms.CharField(
                widget = forms.PasswordInput
                        (attrs = {'class': "form-control",
                                  'placeholder': 'Password *'}))

    password2 = forms.CharField(
                widget = forms.PasswordInput
                        (attrs = {'class': "form-control",
                                  'placeholder': 'Repeat Password *'}))
    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]
        
    def clean_username(self):
        try:
            user = User.objects.get(username__iexact = self.cleaned_data['username'])
        except User.DoesNotExist:
            return self.cleaned_data['username']
        raise forms.ValidationError(_("The username already exists. Please try another one."))

##    def clean_email(self):
##        email = self.cleaned_data['email']
##        try:
##            user = User.objects.get(email=email)
##            raise forms.ValidationError("This email already exists. Did you forget your password?")
##        except User.DoesNotExist:
##            return email
##        raise forms.ValidationError('Duplicate email')

    def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        user.email = self.cleaned_data["email"]
        user.is_active = True #change to False if using email activation
        if commit:
            user.save()
            
        return user

    def clean(self):
        if 'password1' in self.cleaned_data and 'password2' in self.cleaned_data:
            if self.cleaned_data['password1'] != self.cleaned_data['password2']:
                raise forms.ValidationError(_("The two password fields did not match."))
        return self.cleaned_data


class RegistrationFormTermsOfService(RegistrationForm):
    """
    Subclass of ``RegistrationForm`` which adds a required checkbox
    for agreeing to a site's Terms of Service.
    
    """
    tos = forms.BooleanField(widget=forms.CheckboxInput,
                             label=_(u'I have read and agree to the Terms of Service'),
                             error_messages={'required': _("You must agree to the terms to register")})

class RegistrationFormUniqueEmail(RegistrationForm):
    """
    Subclass of ``RegistrationForm`` which enforces uniqueness of
    email addresses.
    
    """
    def clean_self(self):
        """
        Validate that the supplied email address is unique for the site
        """
        if User.objects.filter(email__iexact=self.cleaned_data['email']):
            raise forms.ValidationError(_("This email address is already in use. Please supply a different email address."))
        return self.cleaned_data['email']

class RegistrationFormNoFreeEmail(RegistrationForm):
    """
    Subclass of ``RegistrationForm`` which disallows registration with
    email addresses from popular free webmail services; moderately
    useful for preventing automated spam registrations.
    
    To change the list of banned domains, subclass this form and
    override the attribute ``bad_domains``.
    
    """

    bad_domains = ['aim.com', 'aol.com', 'email.com', 'gmail.com',
                   'googlemail.com', 'hotmail.com', 'hushmail.com',
                   'msn.com', 'mail.ru', 'mailinator.com', 'live.com',
                   'yahoo.com']

    def clean_email(self):
        """
        Check the supplied email address against a list of known free
        webmail domains.
        
        """
        email_domain = self.cleaned_data['email'].split('@')[1]
        if email_domain in self.bad_domains:
            raise forms.ValidationError(_("Registration using free email addresses is prohibited. Please supply a different email address."))
        return self.cleaned_data['email']