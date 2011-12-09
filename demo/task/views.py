from django.shortcuts import render, redirect
from django.forms.models import modelformset_factory
from django.core.urlresolvers import reverse

from demo.task.models import UserTask
from demo.point import helpers as point_helpers

def home(request):
	context = {}
	user = request.user
	if user.is_authenticated():
		TaskFormSet = modelformset_factory(UserTask,fields=['task','length'])
		task_formset = TaskFormSet(request.POST or None,queryset=UserTask.objects.none())
		context['task_formset'] = task_formset

		if request.POST and task_formset.is_valid():
			instances = task_formset.save(commit=False)

			for i in instances:
				i.user = request.user
				i.save()
				point_helpers.Task().grant_points()

			return redirect(reverse('home'))

	return render(request, 'home.html', context)
