from django.conf import settings

def google_key(request):
	return { 'GOOGLE_KEY': settings.GOOGLE_KEY }
