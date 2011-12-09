from django.shortcuts import render,redirect
from django.core.urlresolvers import reverse
from django.contrib import messages

def login(request):
	return redirect(reverse('home'))


