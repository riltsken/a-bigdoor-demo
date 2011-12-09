from django.conf.urls.defaults import *
from django.views.generic.base import TemplateView

urlpatterns = patterns('demo.base.views',
    url(r'^about/$',	TemplateView.as_view(template_name='about.html'),		name="about"),
)
