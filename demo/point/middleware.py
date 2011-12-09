from datetime import datetime, timedelta

from django.contrib import messages
from restkit import resource

from demo.point.helpers import PointAssigner

""" Middleware checking for the last time a user came to the site.
We create a check in the session so that we don't have to call the BigDoor API so much.
"""
class DailyCheckIn(object):

	def process_request(self,request):
		if request.user.is_authenticated():
			if not request.session.get('last_check_in') or (request.session.get('last_check_in') < datetime.now() - timedelta(days=1)):
				checkin = PointAssigner('checkin',request.user.username)
				try:
					status_code = checkin.grant_points()
					messages.info(request, "You just got points for checking in today!")
				except resource.RequestFailed, e:
					if e.msg == '3':
						request.session['last_check_in'] = datetime.now()
					else:
						raise e

