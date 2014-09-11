from django.conf.urls import patterns, url, include
from farmers import views
from rest_framework.routers import DefaultRouter
from agriapi import settings

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'farmers', views.FarmerViewSet)
router.register(r'users', views.UserViewSet)
router.register(r'receipts', views.ReceiptViewSet)
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
    url(r'^get-key/', 'rest_framework.authtoken.views.obtain_auth_token'),
)

urlpatterns += patterns('',  
    (r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),  
)  
