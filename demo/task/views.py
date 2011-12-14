from django.shortcuts import render, redirect
from django.forms.models import modelformset_factory
from django.core.urlresolvers import reverse

from demo.task.models import UserTask,Task
from demo.point import helpers as point_helpers
from demo.point import models as point_models

""" Either a sign-in page or a users home page

	When showing this page we have the tasks a user can enter
	for gaining XP. Using a formset to leverage multiple model forms
	and javascript to create them.
"""
def home(request):
	context = {}
	user = request.user
	if user.is_authenticated():
		TaskFormSet = modelformset_factory(UserTask,fields=['task','length'])
		task_formset = TaskFormSet(request.POST or None,queryset=UserTask.objects.none())

		if request.POST and task_formset.is_valid():


			""" We need a data structure that looks like this to
				calculate xp points when saving because each task
				is worth a varying amount

				task_amounts = {
					2: {'amount': 5, 'bd_id': 231232},
					5: {'amount': 2, 'bd_id': 232554},
					7: {'amount': 5, 'bd_id': 234466}
				}
			"""
			client = point_helpers.BigDoorClient(request.user.username)
			bd_transactions = client.api.get('named_transaction_group')

			tasks_by_bdid = dict([(t.transaction.bd_id, t.id) for t in Task.objects.all().select_related('transaction')])
			task_amounts = {}
			for trans in bd_transactions[0]:
				named_t = trans['named_transactions'][0]
				task = tasks_by_bdid.get(trans['id'])
				if task:
					task_amounts[task] = {'bd_id': trans['id'], 'amount': named_t['default_amount']}


			instances = task_formset.save(commit=False)
			for i in instances:
				i.user = request.user
				i.save()

				xp_points = task_amounts[i.task_id]['amount'] * i.length # length of time gives more xp

				point_helpers.PointAssigner(request.user.username,
					).grant_points(amount=xp_points,transaction_id=task_amounts[i.task_id]['bd_id'])

			return redirect(reverse('home'))

		# template context
		context['task_formset'] = task_formset
		context['recent_tasks'] = UserTask.objects.filter(user=request.user).select_related('task','user').order_by('-timestamp','-pk')[:8]

	return render(request, 'home.html', context)
