from django.shortcuts import render, redirect
from django.views import generic
from django.utils import translation
from django.utils.translation import ugettext_lazy as _

from django.utils.translation import (
    LANGUAGE_SESSION_KEY, check_for_language, get_language,
)

from django.utils.http import url_has_allowed_host_and_scheme
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.conf import settings

from django.urls import translate_url, reverse

from .forms import ProposalForm
from .models import Proposal, Staff

from django.contrib import messages


class MainPageView(generic.TemplateView):
	template_name = 'main/main.html'

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['main_url'] = reverse('main')
		context['form'] = ProposalForm()
		context['staff'] = Staff.objects.all()[:3]
		return context

class ActivateLanguageView(generic.base.View):

	next_url = ''
	lang_code = ''

	def get(self, request, *args, **kwargs):
		self.next_url = request.META.get('HTTP_REFERER')
		self.lang_code = kwargs.get('lang_code')

		if self.next_url:
			trans_url = translate_url(self.next_url, self.lang_code)
			response = HttpResponseRedirect(self.next_url)
			if trans_url != self.next_url:
				response = HttpResponseRedirect(trans_url)
			response.set_cookie(
				settings.LANGUAGE_COOKIE_NAME, self.lang_code,
				max_age=settings.LANGUAGE_COOKIE_AGE,
				path=settings.LANGUAGE_COOKIE_PATH,
				domain=settings.LANGUAGE_COOKIE_DOMAIN,
				secure=settings.LANGUAGE_COOKIE_SECURE,
				httponly=settings.LANGUAGE_COOKIE_HTTPONLY,
				samesite=settings.LANGUAGE_COOKIE_SAMESITE,
			)
		return response

def form_handler(request):
	page_from = request.META.get('HTTP_REFERER')
	if request.method == 'POST':
		form = ProposalForm(request.POST)
		if form.is_valid():
			Proposal.objects.create(
				name=form.cleaned_data['name'],
				phone=form.cleaned_data['phone'],
				email=form.cleaned_data['email'],
				text=form.cleaned_data['text'],
				page_from=page_from
			)
			messages.success(request, message=_('Заявка уcпешно отправлена!'))
			return redirect(page_from)
		messages.warning(request, message=_('Произошла ошибка!'))
		return redirect(page_from)