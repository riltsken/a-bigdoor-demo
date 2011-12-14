from demo.base.helpers import get_profile_image

""" Gets a users twitter profile img for use on the top bar
"""
def profile_image(request):
	if request.user.is_authenticated():
		return {'profile_image_url': get_profile_image(request.user)}
	return {}

