from django.conf.urls import patterns, url, include
from django.contrib import admin
from django.contrib.auth.models import User
from django.views.generic import RedirectView
from django.views.generic.base import TemplateView
admin.autodiscover()

from farmers import views
#from farmers.views import *

from harvestapi import settings

from password_policies.urls import *

from registration import views as r_views
from registration.backends.default import views as backend_r_view
from registration.backends.default import urls

from rest_framework.routers import DefaultRouter

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
        backend_r_view.RegistrationView.as_view(),
        name='registration_register'),
    url(r'^$', RedirectView.as_view(url='/home/')),
    url(r'^data/', include(router.urls)),
    url(r'^docs/', include('rest_framework_swagger.urls')),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^user/', include('registration.backends.default.urls')),
    url(r'^password/', include('password_policies.urls')),
    #url(r'^signup/', include('farmers.views.registration')),
    url(r'^get-key/', 'rest_framework.authtoken.views.obtain_auth_token'),
    url(r'^api-auth/logout/?next=home/$', 'logout', name='logout'),
    # url(r'^$', '{{ project_name }}.views.home', name='home'),
    # url(r'^{{ project_name }}/', include('{{ project_name }}.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)

urlpatterns += patterns('',  
    (r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),  
)  
