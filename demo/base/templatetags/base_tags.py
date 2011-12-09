from django import template
from django.conf import settings

import simplejson

from bigdoorkit import client

register = template.Library()

@register.inclusion_tag('level.html',takes_context=True)
def render_level(context):
	extra_context = {}

	auth = [
		settings.BIGDOOR_SECRET_KEY,
		settings.BIGDOOR_APPLICATION_KEY
	]
	api = client.Client(*auth)
	endpoint = 'end_user/%s' % context['user'].username
	summary = api.get(endpoint)

	extra_context['next_level_xp'] = 25
	extra_context['level'] = 1
	for level in summary[0]['level_summaries']:
		pass

	extra_context['xp'] = 0
	for currency in summary[0]['currency_balances']:
		if currency['end_user_title'] == 'XP':
			extra_context['xp'] =  currency['current_balance']

	return extra_context

