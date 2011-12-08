from django.conf.urls.defaults import *

urlpatterns = patterns('demo.task.views',
    url(r'^$',			'home',			name="home"),
)
