from django.conf.urls.defaults import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
	(r'^',					include('demo.base.urls')),
	(r'^',					include('demo.task.urls')),
	(r'^twitter/',			include('twython_django_oauth.urls')),
	(r'^points/',			include('point.urls')),
	url(r'^admin/',			include(admin.site.urls)),
) + staticfiles_urlpatterns()
