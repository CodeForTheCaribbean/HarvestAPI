from django import forms
from django.contrib.auth.models import User
from django.core import validators
from django.utils.translation import ugettext_lazy as _
from django.conf import settings

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
   
class PasswordResetForm(forms.Form):
    
    email = forms.EmailField(
                widget = forms.TextInput
                        (attrs = {'class': "form-control",
                                  'placeholder': 'Email *'}))    

    error_messages = {'unknown': ("That email address doesn't have an associated "
                                  "user account. Are you sure you've registered?"),
                      'unusable': ("The user account associated with this email "
                                   "address cannot reset the password."),}
    
    class Meta:
        model = User
        fields = ("email")
        
    def clean_email(self):
        """
        Validates that an active user exists with the given email address.
        """
        UserModel = get_user_model()
        user_email = self.cleaned_data["email"]
        
        
class SetPasswordForm(forms.Form):
    
    new_password1= forms.CharField(
                    widget = forms.PasswordInput
                    (attrs = {'class': "form-control",
                              'placeholder': 'New Password *'}))
        
    new_password2= forms.CharField(
                    widget = forms.PasswordInput
                    (attrs = {'class': "form-control",
                              'placeholder': 'Repeat New Password *'})) 
    
    def clean_new_password2(self):
        password1 = self.cleaned_data.get('new_password1')
        password2 = self.cleaned_data.get('new_password2')
        
        if password1 and password2:
            if password1 != password2:
                raise forms.ValidationError(
                    self.error_messages['password_mismatch'],
                    code='password_mismatch',
                )
        return password2 
    
    def save(self, commit=True):
        self.user.set_password(self.cleaned_data['new_password1'])
        if commit:
            self.user.save()
        return self.user   