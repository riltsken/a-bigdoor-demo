from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('demo.point.views',
   url(r'^awards/',	'awards',	name="point_awards"),
)
