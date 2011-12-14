from decimal import Decimal

from django import template
from django.conf import settings

import simplejson
from bigdoorkit import client

from demo.point import models as point_models

register = template.Library()

@register.inclusion_tag('level.html',takes_context=True)
def render_level(context):
	extra_context = {}

	auth = [
		settings.BIGDOOR_SECRET_KEY,
		settings.BIGDOOR_APPLICATION_KEY
	]
	api = client.Client(*auth)

	""" Calculate XP """
	user_endpoint = 'end_user/%s' % context['user'].username
	summary = api.get(user_endpoint)

	extra_context['xp'] = 0
	for currency in summary[0]['currency_balances']:
		if currency['end_user_title'] == 'XP':
			extra_context['xp'] =  Decimal(currency['current_balance'])

	""" Calculate the users level """
	xp_level_collection = point_models.Level.objects.get(name='xp')
	level_endpoint = 'named_level_collection/%s' % xp_level_collection.bd_id
	levels = api.get(level_endpoint)

	#establish some defaults
	extra_context['next_level_xp'] = levels[0]['named_levels'][0]['threshold']
	extra_context['level'] = 0

	for x, level in enumerate(levels[0]['named_levels']):
		if extra_context['xp'] > level['threshold']:
			extra_context['level'] = x + 1 # enumerate starts at 0
			try:
				extra_context['next_level_xp'] = levels[0]['named_levels'][x + 1]['threshold']
			except IndexError:
				extra_context['next_level_xp'] = 99999

			current_level_threshold = levels[0]['named_levels'][x]['threshold']
			extra_context['xp_bar_current'] = ((extra_context['xp'] - current_level_threshold) / (extra_context['next_level_xp'] - current_level_threshold)) * 100
			extra_context['xp_bar_end'] = 100

	return extra_context

