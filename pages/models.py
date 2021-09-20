from django.db import models
from django_quill.fields import QuillField
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _

class Page(models.Model):
	title = models.CharField(max_length=200, verbose_name=_('Заголовок'))
	slug = models.SlugField(unique=True, verbose_name=_('ID'))
	description = models.CharField(max_length=600, verbose_name=_('Описание'))
	text = QuillField(verbose_name=_('Текст'))
	active = models.BooleanField(default=True)

	def get_absolute_url(self):
		return reverse('page', kwargs={'slug': self.slug})


	def __str__(self):
		return self.title

	class Meta:
		verbose_name = 'страница'
		verbose_name_plural = 'страницы'