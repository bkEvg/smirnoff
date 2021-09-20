from django.shortcuts import render
from django.views.generic import TemplateView
from django.urls import reverse


class KitchenView(TemplateView):
	template_name = 'kitchen/kitchen.html'

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['kitchen_url'] = reverse('kitchen')
		return context