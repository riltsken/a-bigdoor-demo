from django.shortcuts import render,redirect
from django.core.urlresolvers import reverse
from django.contrib import messages

from demo.point.helpers import BigDoorClient

def awards(request):
	client = BigDoorClient(request.user.username)
	user = client.api.get('end_user/%s' % request.user.username)
	awards = user[0]['award_summaries']
	return render(request,'point/awards.html', {'awards': awards})
