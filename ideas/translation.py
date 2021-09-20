from modeltranslation.translator import translator, TranslationOptions
from .models import Galery

class GaleryTranslationOptions(TranslationOptions):
	fields = ('title',)

translator.register(Galery, GaleryTranslationOptions)