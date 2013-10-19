from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()
from reader.views import ReadJson, upload_file

urlpatterns = patterns('',
                       url(r'^$', ReadJson.as_view(), name='home'),
                       url(r'^upload/$', upload_file),
                       )
