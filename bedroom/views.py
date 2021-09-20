from django.shortcuts import render
from django.views.generic import TemplateView
from django.urls import reverse


class BedroomView(TemplateView):
	template_name = 'bedroom/bedroom.html'

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['bedroom_url'] = reverse('bedroom')
		return context
