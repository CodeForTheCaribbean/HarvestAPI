from django.conf.urls import patterns, url, include
from farmers import views
#from farmers import templates
from rest_framework.routers import DefaultRouter
from harvestapi import settings
from django.contrib.auth.models import User
from django.views.generic.base import TemplateView
from farmers.views import RegistrationView, ActivationView
from farmers.views import PasswordResetConfirmView
from farmers.views import PasswordResetFormView
from django.views.generic import RedirectView
from password_policies.views import *
from password_policies.urls import *

from django.contrib import admin
admin.autodiscover()

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'farmers', views.FarmerViewSet)
#router.register(r'users', views.UserViewSet)
#router.register(r'receipts', views.ReceiptViewSet)
router.register(r'farms', views.FarmViewSet)
router.register(r'crops', views.CropViewSet)
router.register(r'livestock', views.LivestockViewSet)
router.register(r'prices', views.PriceViewSet)

# The API URLs are now determined automatically by the router.
# Additionally, we include the login URLs for the browseable API.
# Included docs URL to 'swagger' docs
urlpatterns = patterns('',
    url(r'^home/$',
        RegistrationView.as_view(),
        name='registration_register'),
    url(r'^$', RedirectView.as_view(url='/home/')),
    url(r'^data/', include(router.urls)),
    url(r'^docs/', include('rest_framework_swagger.urls')),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    #url(r'^users/register', 'farmers.views.register'),
    url(r'^user/', include('registration.backends.default.urls')),
    url(r'^password/', include('password_policies.urls')),
    #url(r'^signup/', include('farmers.views.registration')),
    url(r'^get-key/', 'rest_framework.authtoken.views.obtain_auth_token'),
    # url(r'^$', '{{ project_name }}.views.home', name='home'),
    # url(r'^{{ project_name }}/', include('{{ project_name }}.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    
    url(r'^user/activate/complete/$',
        TemplateView.as_view(template_name='registration/activation_complete.html'),
        name='registration_activation_complete'),
    
    # Activation keys get matched by \w+ instead of the more specific
    # [a-fA-F0-9]{40} because a bad activation key should still get to the view;
    # that way it can return a sensible "invalid key" message instead of a
    # confusing 404.    
    url(r'^user/activate/(?P<activation_key>\w+)/$',
        ActivationView.as_view(),
        name='registration_active'),
    
    url(r'^user/register/$',
        RegistrationView.as_view(),
        name='registration_register'),
    
    url(r'^user/register/complete/#signup$',
        TemplateView.as_view(template_name='registration/registration_complete.html'),
        name='registration_complete'),
    
    url(r'^register/closed/$',
        TemplateView.as_view(template_name='registration/registration_closed.html'),
        name='registration_disallowed'),   
)

urlpatterns += patterns('',  
    (r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),  
)  
