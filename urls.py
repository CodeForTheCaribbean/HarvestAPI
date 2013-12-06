from django.conf.urls import patterns, url, include
from farmers import views
from rest_framework.routers import DefaultRouter

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'farmers', views.FarmerViewSet)
router.register(r'users', views.UserViewSet)
router.register(r'receipts', views.ReceiptViewSet)

# The API URLs are now determined automatically by the router.
# Additionally, we include the login URLs for the browseable API.
# Included docs URL to 'swagger' docs
urlpatterns = patterns('',
    url(r'^', include(router.urls)),
    url(r'^docs/', include('rest_framework_swagger.urls')),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))

)
