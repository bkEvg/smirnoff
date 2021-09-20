from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Galery


class IdeasView(ListView):
	model = Galery
	template_name = 'ideas/ideas_list.html'
	context_object_name = 'galeries'


class IdeasDetailView(DetailView):
	model = Galery
	template_name = 'ideas/ideas_detail.html'
	context_object_name = 'galery'