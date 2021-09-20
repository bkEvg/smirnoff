from django.db import models
from django.utils.translation import ugettext_lazy as _


class Staff(models.Model):
	image = models.ImageField(upload_to='staff_images/', blank=False, verbose_name=_('Фото сотрудника'))
	position = models.CharField(max_length=150, verbose_name=_('Должность'))
	first_name = models.CharField(max_length=150, verbose_name=_('Имя'))
	last_name = models.CharField(max_length=150, verbose_name=_('Фамилия'))
	notation = models.CharField(max_length=900, verbose_name=_('Цитата'))


	def get_full_name(self):
		if self.first_name and self.last_name:
			return '{0} {1}'.format(self.first_name, self.last_name)
		else:
			return self.first_name

	def __str__(self):
		return self.first_name

	class Meta:
		verbose_name = _('сотрудник')
		verbose_name_plural = _('сотрудники')

class Proposal(models.Model):
	name = models.CharField(max_length=150)
	phone = models.CharField(max_length=18)
	email = models.EmailField()
	text = models.TextField(blank=True)
	date_created = models.DateTimeField(auto_now_add=True)
	date_updated = models.DateTimeField(auto_now=True)
	page_from = models.CharField(max_length=500)

	def __str__(self):
		return self.name

	class Meta:
		verbose_name = _('заявку')
		verbose_name_plural = _('заявки')

