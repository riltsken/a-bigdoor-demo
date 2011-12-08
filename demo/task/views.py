from django.shortcuts import render
from django.forms.models import modelformset_factory

def home(request):
	context = {}
	user = request.user
	if user.is_authenticated():

		form

	return render(request, 'home.html', context)
