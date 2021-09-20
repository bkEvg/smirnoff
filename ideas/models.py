from django.db import models
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _


class Galery(models.Model):
	title = models.CharField(max_length=150, verbose_name=_('Название альбома'))

	def get_absolute_url(self):
		return reverse('ideas_detail', kwargs={'pk': self.pk})

	def __str__(self):
		return self.title

	class Meta:
		verbose_name = 'альбом'
		verbose_name_plural = 'альбомы'


class Photo(models.Model):
	image = models.ImageField(upload_to='ideas/photos/%j_%M_%Y/', verbose_name=_('Фото'))
	album = models.ForeignKey(Galery, on_delete=models.CASCADE, related_name='photos', verbose_name=_('Альбом'), blank=False, null=True)

