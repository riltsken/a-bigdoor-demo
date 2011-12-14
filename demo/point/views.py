from django.shortcuts import render,redirect
from django.core.urlresolvers import reverse
from django.contrib import messages

from demo.point.helpers import BigDoorClient

def awards(request):
	client = BigDoorClient(request.user.username)
	user = client.api.get('end_user/%s' % request.user.username)
	awards = []

	# these are custom named awards
	awards.extend(user[0]['award_summaries'])

	# these are awards assigned via leveling up in different categories
	awards.extend(user[0]['level_summaries'][::-1])
	return render(request,'point/awards.html', {'awards': awards})
