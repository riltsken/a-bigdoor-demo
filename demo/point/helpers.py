from django.conf import settings

from bigdoorkit import client

from demo.point import models as pmodels

class BigDoorClient(object):
	auth = [
		settings.BIGDOOR_SECRET_KEY,
		settings.BIGDOOR_APPLICATION_KEY
	]

	def __init__(self,username):
		self.api = client.Client(*self.auth)
		self.username = username

class AwardAssigner(BigDoorClient):
	def __init__(self,award,*args,**kwargs):
		super(AwardAssigner,self).__init__(*args,**kwargs)
		self.award_id = self.get_award()

	def get_award(self):
		return pmodels.Award.objects.get(name=self.award).bd_id

	def grant_award(self):
		endpoint = 'end_user/%s/award/%s' % (self.award_id,self.username)
		return self.api.post(endpoint)

class PointAssigner(BigDoorClient):

	def __init__(self,transaction,*args,**kwargs):
		super(PointAssigner,self).__init__(*args,**kwargs)
		self.transaction_id = self.get_transaction(transaction)

	def get_transaction(self,transaction):
		return pmodels.Transaction.objects.get(name=transaction).bd_id

	def grant_points(self):
		endpoint = 'named_transaction_group/%s/execute/%s' % (self.transaction_id,self.username)
		return self.api.post(endpoint)

