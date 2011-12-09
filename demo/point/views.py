from django.shortcuts import render,redirect
from django.core.urlresolvers import reverse
from django.contrib import messages

def login(request):
	#c = CheckIn(request.user.username)
	#c.grant_points()
	#messages.success(request,c.success_message)
	return redirect(reverse('home'))


