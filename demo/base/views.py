from demo.point.helpers import AwardAssigner

def about(request):

	AwardAssigner('about',request.user.username)
	messages.info(request, "You just got an award for checking out this page!")
	return render(request,'about.html',context)
