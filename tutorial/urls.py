from django.conf.urls import patterns, include, url
from rest_framework.urlpatterns import format_suffix_patterns

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('snippets.views',
    url(r'^snippets/$', 'snippet_list'),
    url(r'^snippets/(?P<pk>[0-9]+)$', 'snippet_detail'),
)

urlpatterns = format_suffix_patterns(urlpatterns)


