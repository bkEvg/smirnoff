from .models import Page

def pages(request):
	return {'pages': Page.objects.filter(active=True)}