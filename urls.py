from django.conf.urls import patterns, url, include
from farmers import views
#from farmers import templates
from rest_framework.routers import DefaultRouter
from harvestapi import settings
from django.contrib.auth.models import User
from registration.views import *

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
    url(r'^', include(router.urls)),
    url(r'^docs/', include('rest_framework_swagger.urls')),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^users/register', 'farmers.views.register'),
    url(r'^user/', include('registration.backends.default.urls')),
    #url(r'^signup/', include('farmers.views.registration')),
    url(r'^get-key/', 'rest_framework.authtoken.views.obtain_auth_token'),
    # url(r'^$', '{{ project_name }}.views.home', name='home'),
    # url(r'^{{ project_name }}/', include('{{ project_name }}.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^user/register_here', 'farmers.views.register_here'),
    url(r'^user/register_complete', 'farmers.views.register_success'),
    ##    url(r'^user/confirm/(?P<activation_key>\w+)/', 'farmers.views.activate')
)

urlpatterns += patterns('',  
    (r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),  
)  
