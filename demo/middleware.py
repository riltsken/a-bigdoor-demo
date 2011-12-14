from django.shortcuts import render
from django.contrib import messages

PARSE_ERRORS = [
"Caught ParserError while rendering: nparsed != recved",
"Caught ValueError while rendering: No JSON object could be decoded",
]

class BigDoorParseError(object):

	def process_exception(self, request, exception):
		print "%s --\n MESSAGE: %s" % (exception,exception.message)
		if exception.message in PARSE_ERRORS:
			messages.error(request,"There was an error receiving data from BigDoor")
			return render(request, 'extended_500.html', {})
