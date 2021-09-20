from django.shortcuts import render
from django.views import View
from .models import Page
from django.http import HttpResponse


class PageView(View):
	def get(self, request, *args, **kwargs):
		context = {'page': Page.objects.get(slug=kwargs['slug'])}
		return render(request, 'pages/page.html', context=context)

