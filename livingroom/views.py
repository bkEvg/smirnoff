from django.shortcuts import render
from django.views import generic
from django.urls import reverse


class LivingroomView(generic.TemplateView):
	template_name = 'livingroom/living.html'

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['living_url'] = reverse('livingroom')
		return context