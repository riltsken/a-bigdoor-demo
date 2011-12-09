from django.db import models
from django.contrib.auth.models import User

class Task(models.Model):
	name = models.CharField(max_length=100)

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
