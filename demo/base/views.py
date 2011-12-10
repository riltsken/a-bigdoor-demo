from django.contrib import messages
from django.shortcuts import render

from demo.point.helpers import AwardAssigner

def about(request):
	context = {}
	if request.user.is_authenticated():
		award_assigner = AwardAssigner('about_page',request.user.username)
		if not award_assigner.has_award():
			award_assigner.grant_award()
			messages.info(request, "You just got an award for checking out this page!")
	return render(request,'about.html',context)
