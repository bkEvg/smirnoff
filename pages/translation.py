from modeltranslation.translator import translator, TranslationOptions
from .models import Page

class PageTranslationOption(TranslationOptions):
	fields = ('title', 'description', 'text')
	
translator.register(Page, PageTranslationOption)