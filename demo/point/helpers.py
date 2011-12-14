from django.conf import settings

from bigdoorkit import client

from demo.point import models as pmodels

""" Generic way for distributing points or awards to users
"""
class BigDoorClient(object):
	auth = [
		settings.BIGDOOR_SECRET_KEY,
		settings.BIGDOOR_APPLICATION_KEY
	]

	def __init__(self,username):
		self.api = client.Client(*self.auth)
		self.username = username

class AwardAssigner(BigDoorClient):
	def __init__(self,username,award,*args,**kwargs):
		super(AwardAssigner,self).__init__(username,*args,**kwargs)
		self.award_id = self.get_award(award)

	def get_award(self,award):
		return pmodels.Award.objects.get(name=award).bd_id

	def has_award(self):
		endpoint = 'end_user/%s/award' % self.username
		awards = self.api.get(endpoint)
		for award in awards[0]:
			if award['named_award_id'] == self.award_id:
				return True

		return False

	def grant_award(self):
		endpoint = 'end_user/%s/award' % self.username
		return self.api.post(endpoint, {}, {'named_award_id': self.award_id})

class PointAssigner(BigDoorClient):
	def __init__(self,username,transaction=None,*args,**kwargs):
		super(PointAssigner,self).__init__(username,*args,**kwargs)
		self.transaction_id = None
		if transaction:
			self.transaction_id = self.get_transaction(transaction)

	def get_transaction(self,transaction):
		return pmodels.Transaction.objects.get(name=transaction).bd_id

	def grant_points(self,amount=None,transaction_id=None):
		tid = transaction_id or self.transaction_id

		# sanity check
		assert tid is not None

		endpoint = 'named_transaction_group/%s/execute/%s' % (tid,self.username)
		if amount:
			return self.api.post(endpoint,{},{'amount': amount})
		return self.api.post(endpoint)

