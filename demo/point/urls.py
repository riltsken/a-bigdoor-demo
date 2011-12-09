from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('demo.point.views',
   url(r'^login/',	'login',	name="points_login"),
)
