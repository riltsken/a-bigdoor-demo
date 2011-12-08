from django.db import models
from django.dispatch import receiver
from django.contrib.auth.models import User
from django.conf import settings

from bigdoorkit import client

@receiver(models.signals.post_save, sender=User)
def create_bigdoor_user(sender, **kwargs):
	if kwargs['created']:
		auth = [
			settings.BIGDOOR_SECRET_KEY,
			settings.BIGDOOR_APPLICATION_KEY
		]
		api = client.Client(*auth)
		endpoint = 'end_user/%s' % kwargs['instance'].username
		api.put(endpoint)
