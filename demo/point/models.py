from django.db import models

class BigDoorModel(models.Model):
	bd_id = models.CharField(max_length=40)

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
