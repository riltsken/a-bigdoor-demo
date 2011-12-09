from django.conf.urls.defaults import *
from django.views.generic.base import TemplateView

urlpatterns = patterns('demo.base.views',
    url(r'^about/$',	'about',		name="about"),
)
