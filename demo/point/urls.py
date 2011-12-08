from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('demo.points.views',
   url(r'^login/',	'login',	name="points_login"),
)
