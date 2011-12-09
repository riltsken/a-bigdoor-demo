from django.conf import settings

from bigdoorkit import client

from demo.point import models as pmodels

class PointAssigner(object):
	currency = None
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
		if not self.currency:
			raise ValueError("Currency must be set on this object to assign points properly")
		return pmodels.Currency.objects.get(name=self.currency).bd_id

	def grant_points(self):
		endpoint = 'named_transaction_group/%s/execute/%s' % (self.currency_id,self.username)
		api.post(endpoint)

class CheckIn(PointAssigner):
	currency = 'checkin'

	def success_message(self):
		return "You just got points for checking in today!"

class Task(PointAssigner):
	currency = 'xp'

	def success_message(self):
		return "You just got points for completing some tasks!"

