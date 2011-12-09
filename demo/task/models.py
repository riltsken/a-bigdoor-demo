from datetime import date

from django.db import models
from django.contrib.auth.models import User

from demo.point.models import Transaction

class Task(models.Model):
	name = models.CharField(max_length=100)
	transaction = models.ForeignKey(Transaction)

	def __unicode__(self):
		return self.name

class UserTask(models.Model):
	LENGTH_CHOICES = (
		(1,'1 hour or less'),
		(2,'2 hours'),
		(3,'3 hours'),
		(4,'4 hours'),
		(5,'5 hours'),
		(6,'6 hours'),
		(7,'7 hours'),
		(8,'8 hours'),
		(9,'More than 8 hours')
	)

	user = models.ForeignKey(User)
	task = models.ForeignKey(Task)
	length = models.IntegerField(choices=LENGTH_CHOICES)
	timestamp = models.DateField(default=date.today)

	def __unicode__(self):
		return "%s by %s for %s hours on %s" % (self.task, self.user.username, self.length, self.timestamp)
