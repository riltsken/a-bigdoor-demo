from django.conf.urls.defaults import *

urlpatterns = patterns('demo.base.views',
    url(r'^about/$',		'about',			name="base_about"),
    url(r'^leaderboard/$',	'leaderboard',		name="base_leaderboard"),
)
