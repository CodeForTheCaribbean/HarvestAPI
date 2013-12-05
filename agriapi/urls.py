from django.conf.urls import patterns, include, url
from rest_framework.urlpatterns import format_suffix_patterns

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('farmers.views',
    url(r'^farmers/$', 'farmer_list'),
    url(r'^farmers/(?P<pk>[0-9]+)$', 'farmer_id'),
)

urlpatterns = format_suffix_patterns(urlpatterns)


