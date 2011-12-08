from django.shortcuts import render,redirect
from django.core.urlresolvers import reverse
from django.contrib import messages
from django.conf import settings

from bigdoorkit import client

from demo.points import models as pmodels

# username,currency_id,message
class PointAssigner(object):
	auth = [
		settings.BIGDOOR_SECRET_KEY,
		settings.BIGDOOR_APPLICATION_KEY
	]

	def __init__(self,username):
		self.api = client.Client(*self.auth)
		self.username = username
		self.currency_id = self.get_currency()

	def success_message(self):
		return "You have been granted points!"

	def get_currency(self):
		raise NotImplementedError

	def grant_points(self):
		endpoint = 'named_transaction_group/%s/execute/%s' % (self.currency_id,self.username)
		api.post(endpoint)

class CheckIn(PointAssigner):
	def success_message(self):
		return "You just got points for checking in today!"

	def get_currency(self):
		return pmodels.Currency.objects.get(name='checkin').pk

def login(request):
	#c = CheckIn(request.user.username)
	#c.grant_points()
	#messages.success(request,c.success_message)
	return redirect(reverse('home'))


