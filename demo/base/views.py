from django.contrib import messages
from django.shortcuts import render
from django.contrib.auth.models import User

from demo.base import helpers as bhelpers
from demo.point import helpers as phelpers
from demo.point import models as pmodels

""" Get an award for reading the about page :)
"""
def about(request):
	context = {}
	if request.user.is_authenticated():
		award_assigner = phelpers.AwardAssigner(request.user.username,'about_page')
		if not award_assigner.has_award():
			award_assigner.grant_award()
			messages.info(request, "You just got an award for checking out this page!")
	return render(request,'about.html',context)

""" Show the leaderboard based on user XP
"""
def leaderboard(request):
	client = phelpers.BigDoorClient(request.user.username)
	leaderboard = client.api.get('leaderboard/execute',{'filter_value': pmodels.Currency.objects.get(name='xp').bd_id})

	results = []
	app_users = dict((u.username, u) for u in User.objects.filter(twitterprofile__isnull=False).select_related('twitter_profile'))
	for x,user in enumerate(leaderboard[0]['results']):
		app_user = app_users.get(user['end_user_login'])
		profile_image_url = None
		if app_user:
			profile_image_url = bhelpers.get_profile_image(app_user)

		results.append( (x+1, profile_image_url, user['end_user_login'], user['curr_balance']) )

	return render(request,'leaderboard.html', {'results': results})
