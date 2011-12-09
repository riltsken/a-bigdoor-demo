from django.conf import settings

import twython
from twython_django_oauth.models import TwitterProfile

def get_profile_image(user,size="mini"):
	try:
		twitter_profile = user.twitterprofile
		auth = {
			'twitter_token': settings.TWITTER_KEY,
			'twitter_secret': settings.TWITTER_SECRET,
			'oauth_token': twitter_profile.oauth_token,
			'oauth_token_secret': twitter_profile.oauth_secret
		}
		api = twython.Twython(**auth)
		image_url = api.getProfileImageUrl(user.username, size="mini")
	except TwitterProfile.DoesNotExist:
		image_url = None

	return image_url
