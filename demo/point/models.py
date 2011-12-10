from django.db import models

class BigDoorModel(models.Model):
	name = models.CharField(max_length=25)
	bd_id = models.IntegerField()

	def __unicode__(self):
		return self.name

	class Meta:
		abstract = True

class Currency(BigDoorModel):
	pass

class Level(BigDoorModel):
	pass

class Award(BigDoorModel):
	pass

class Transaction(BigDoorModel):
	pass
