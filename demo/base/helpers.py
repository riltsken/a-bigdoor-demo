import twython
from django.conf import settings

def get_profile_image(user,size="mini"):
	twitter_profile = user.twitterprofile
	auth = {
		'twitter_token': settings.TWITTER_KEY,
		'twitter_secret': settings.TWITTER_SECRET,
		'oauth_token': twitter_profile.oauth_token,
		'oauth_token_secret': twitter_profile.oauth_secret
	}
	api = twython.Twython(**auth)
	return api.getProfileImageUrl(user.username, size="mini")
