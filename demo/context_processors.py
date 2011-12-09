from demo.base.helpers import get_profile_image

def profile_image(request):
	if request.user.is_authenticated:
		return {'profile_image_url': get_profile_image(request.user)}
